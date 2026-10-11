import csv
import io
from datetime import datetime
from core.models import db_helper, es_helper, Document
import logging

logger = logging.getLogger(__name__)

async def csv_upload(file_bytes: bytes):
    try:
        f = io.BytesIO(file_bytes)
        text_stream = io.TextIOWrapper(f, encoding='utf-8')

        reader = csv.DictReader(text_stream)

        async with db_helper.session_factory() as session:
            for row in reader:
                try:
                    doc_text = row["text"]
                    doc_date_str = row["created_date"]
                    doc_rubrics_str = row["rubrics"]

                    parsed_date = datetime.strptime(doc_date_str, "%Y-%m-%d %H:%M:%S")

                    import ast
                    parsed_rubrics = ast.literal_eval(doc_rubrics_str)

                    db_document = Document(
                        text=doc_text,
                        created_date=parsed_date,
                        rubrics=parsed_rubrics
                    )
                    session.add(db_document)
                    await session.commit()
                    await session.refresh(db_document)

                    await es_helper.client.index(
                        index='documents',
                        id=str(db_document.id),
                        document={
                            "text": db_document.text
                        }
                    )
                except Exception as row_error:
                    logger.error(row_error)
                    continue
    except Exception as e:
        logger.error(e)