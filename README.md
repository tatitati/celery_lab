Install celery:
```
pip3 install celery

```

Run redis (broker):

```
docker run -d -p 6379:6379 --name redis1 redis
```


Start two servers to process only specific feeds queue:

```
celery -A  tasks worker  -Q low-priority --loglevel=info
celery -A  tasks worker  -Q celery --loglevel=info
celery -A  tasks worker  -Q celery,low-priority --loglevel=info
```


Run invoker:

```
python3 client.py
```


More info here:
https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html