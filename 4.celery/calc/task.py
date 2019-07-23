from celery import Celery
import time
app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
time.sleep(40)
add.delay(3400000,560000)
time.sleep(30)
ans=add.get()
print(ans)