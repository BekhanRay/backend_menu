from decouple import config

PRODUCTION = config('PRODUCTION', cast=bool)
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')

POSTGRES_DB = config('PG_NAME')
POSTGRES_USER = config('PG_USER')
POSTGRES_PASSWORD = config('PG_PASSWORD')
POSTGRES_HOST = config('PG_HOST')
POSTGRES_PORT = config('PG_PORT', cast=int)
