from celery import Celery

app = Celery(...)

@app.task
def add(a, b):
    return a + b