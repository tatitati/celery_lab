import time
from celery import Celery


app = Celery(
	'tasks', 
	broker='redis://localhost:6379/0', # where to send tasks
	backend='redis://localhost:6379/0' # where to store the tasks results
)


@app.task(name='tasks.add')
def add(x, y):
	return x + y	
