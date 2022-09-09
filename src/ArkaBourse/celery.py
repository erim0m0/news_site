import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ArkaBourse.settings')

celery_app = Celery('ArkaBourse')
celery_app.config_from_object('ArkaBourse.celeryconfig')
celery_app.autodiscover_tasks()
