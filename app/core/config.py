from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8080

class ApiPrefix(BaseModel):
    api_pref: str = '/api_v1'
    upload_csv: str = '/upload_csv'
    search: str = '/search'

class DbConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

class EsConfig(BaseModel):
    url: str = 'http://127.0.0.1:9200/'

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file= BASE_DIR / '.env',
        case_sensitive = False,
        env_nested_delimiter='__',
        env_prefix='E_SEARCH__',
    )
    run: RunConfig = RunConfig()
    db: DbConfig
    api_v1: ApiPrefix = ApiPrefix()
    es: EsConfig = EsConfig()


settings = Settings()