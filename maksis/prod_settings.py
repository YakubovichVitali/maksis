from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-$hpzkty&qe(-ha&((51)4tot+18$ee%p8%b6p7c*z5xurc$#fr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    '0.0.0.0',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'maksis',
        'USER': 'vitali',
        'PASSWORD': 'password',
        'HOST': 'db',  # if run without docker, use localhost
        'PORT': 5432,
    }
}
