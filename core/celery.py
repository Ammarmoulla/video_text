import os
from celery import Celery
# from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.conf.task_serializer = 'pickle'
app.conf.result_serializer = 'pickle'

app.conf.accept_content = ['application/json', 'application/x-python-serialize', 'pickle']
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))