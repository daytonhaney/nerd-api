from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="_MaTWSbnfGgwo1LuP3OVX6TQHxIO4xjenHsDNYPZ65Fmd5Pa4DU",
)

# SECURITY WARNING: don't run with debug turned on in production!
# TODO change in prod
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND = "dj_celery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@api.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Nginx Elastic Search Redis Docker Django API"
