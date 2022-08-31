import os
from datetime import timedelta
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ArkaBourse.settings')

celery_app = Celery('ArkaBourse')
celery_app.autodiscover_tasks()
celery_app.conf.update(
    broker_url='redis://localhost//',
    task_serializer='json',
    result_serializer='json',
    accept_content=['json', 'json'],
    result_expires=timedelta(days=1, hours=12),
    task_always_eager=False,
    worker_prefetch_multiplier=4
)
