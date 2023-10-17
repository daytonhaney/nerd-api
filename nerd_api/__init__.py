from .celery import app as celery_app

__all__ = ["celery_app"]

"""
adding as a tuple ("celery_app", ) was giving issues for some reason = 

$ make logs
...
celery_worker   | PostgreSQL is available
celery_worker   | [16:46:26] watchfiles v0.18.1 👀  path="/app" target="celery.__main__.main" (function) filter=DefaultFilter...
celery_worker   | Process SpawnProcess-1:
celery_worker   | Traceback (most recent call last):
celery_worker   |   File "/usr/local/lib/python3.12/site-packages/watchfiles/run.py", line 394, in set_tty
celery_worker   |     with open(tty_path) as tty:  # pragma: no cover
celery_worker   |          ^^^^^^^^^^^^^^
celery_worker   | OSError: [Errno 6] No such device or address: '/dev/tty'
celery_worker   |
celery_worker   | During handling of the above exception, another exception occurred:
celery_worker   |
celery_worker   | Traceback (most recent call last):
celery_worker   |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
celery_worker   |     self.run()
celery_worker   |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
celery_worker   |     self._target(*self._args, **self._kwargs)
celery_worker   |   File "/usr/local/lib/python3.12/site-packages/watchfiles/run.py", line 354, in run_function
celery_worker   |     func(*args, **kwargs)
celery_worker   |   File "/usr/local/lib/python3.12/site-packages/celery/__main__.py", line 14, in main
celery_worker   |     from celery.bin.celery import main as _main
celery_worker   |   File "/usr/local/lib/python3.12/site-packages/celery/bin/celery.py", line 78, in <module>
celery_worker   |     @with_plugins(entry_points().get('celery.commands', []))
celery_worker   |                   ^^^^^^^^^^^^^^^^^^
celery_worker   | AttributeError: 'EntryPoints' object has no attribute 'get'
mailhog        | 2023/10/17 16:53:36 Using in-memory storage

adding as list = 

... 
celery_worker  | PostgreSQL is available
celery_worker  | [16:53:40] watchfiles v0.18.1 👀  path="/app" target="celery.__main__.main" (function) filter=DefaultFilter...
mailhog        | 2023/10/17 16:53:36 Using in-memory storage
"""
