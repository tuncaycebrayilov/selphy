from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
celery_app = Celery("mysite")
celery_app.config_from_object(settings, namespace="CELERY")
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)