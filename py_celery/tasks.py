import os

import time
import celery
# from celery.decorators import task

CELERY_BROKER = os.environ.get('CELERY_BROKER')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND')

app = celery.Celery(
   'tasks',
   broker=CELERY_BROKER,
   backend=CELERY_BACKEND
)


@app.task
def run():
    time.sleep(10)
    print('処理　おわた')
    return 'おわったよ'


@app.task
def calc(a, b):
    return a+b
