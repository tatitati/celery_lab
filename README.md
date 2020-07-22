Install celery:
```
pip3 install celery

```

Run redis (broker):

```
docker run -d -p 6379:6379 --name redis1 redis
```


Start some workers: 3 of them will process tasks sent to low-priority queue, and two will process tasks sent to celery queue

```
cd src
celery -A  tasks worker  -Q celery --loglevel=info
celery -A  tasks worker  -Q low-priority --loglevel=info
celery -A  tasks worker  -Q low-priority --loglevel=info
celery -A  tasks worker  -Q celery,low-priority --loglevel=info
```


Run invoker:

```
cd src
python3 client.py
```


More info here:
https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html