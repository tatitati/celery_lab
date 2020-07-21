Run workers:

```
celery -A  tasks worker  --loglevel=info
```


Run invoker:

```
python3 invoker.py
```