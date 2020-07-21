import time
from celery import Celery


app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')


@app.task(name='tasks.add')
def add(x, y):
	total = x + y
	print('{} + {} = {}'.format(x, y, total))
	time.sleep(10) # I want to simulate a long task
	return total
