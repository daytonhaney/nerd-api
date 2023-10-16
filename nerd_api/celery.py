import os

from celery import Celery
from django.conf import settings

# TODO: change in prod

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nerd_api.settings.local")
app = Celery("nerd_api")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
