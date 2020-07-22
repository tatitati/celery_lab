import time
from celery import Celery


app = Celery(
	'tasks', 
	broker='redis://localhost:6379/0', # where to send tasks (to redis)	
	backend='db+sqlite:///results.db'  # where to store the results (optional)
)

app.config_from_object('celeryconfig')


@app.task(name='tasks.add')
def add(x, y):
	return x + y	


@app.task(name='tasks.sayhi')
def sayhi():
	return "hi!!!!!"	
