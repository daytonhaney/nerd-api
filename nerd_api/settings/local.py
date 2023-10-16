from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="_MaTWSbnfGgwo1LuP3OVX6TQHxIO4xjenHsDNYPZ65Fmd5Pa4DU",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND="dj_celery_email.backends.CeleryEmailBackend"
EMAIL_HOST=env("EMAIL_HOST", default="mailhog")
EMAIL_PORT=env("EMAIL_PORT")
DOMAIN=env("DOMAIN")
SITE_NAME="JPP Site Template"


