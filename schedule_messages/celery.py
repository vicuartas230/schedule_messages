from os import environ
from celery import Celery
from celery.schedules import crontab

environ.setdefault('DJANGO_SETTINGS_MODULE', 'schedule_messages.settings')

app = Celery('schedule_messages')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
