Run redis:

```
docker run -d -p 6379:6379 --name redis1 redis
```


Run workers:

```
celery -A  tasks worker  --loglevel=info
```


Run invoker:

```
python3 invoker.py
```


More info here:
https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html