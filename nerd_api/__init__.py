from .celery import app as celery_app

# __all__ = ["celery_app"]

__all__ = ("celery_app",)


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
celery_worker   | [2023-10-17 16:53:46,194: WARNING/SpawnProcess-1] /usr/local/lib/python3.12/site-packages/celery/worker/consumer/consumer.py:507: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
celery_worker   | whether broker connection retries are made during startup in Celery 6.0 and above.
celery_worker   | If you wish to retain the existing behavior for retrying connections on startup,
celery_worker   | you should set broker_connection_retry_on_startup to True.
celery_worker   |   warnings.warn(
celery_worker   |
celery_worker   | [2023-10-17 16:53:46,203: INFO/SpawnProcess-1] mingle: searching for neighbors
celery_worker   | [2023-10-17 16:53:47,236: INFO/SpawnProcess-1] mingle: all alone
celery_worker   | [2023-10-17 16:53:47,261: INFO/SpawnProcess-1] celery@174e2895e6ed ready.
celery_worker   | [16:57:32] 1 change detected
celery_worker   |
celery_worker   | worker: Hitting Ctrl+C again will terminate all running tasks!
celery_worker   |
celery_worker   | worker: Warm shutdown (MainProcess)
celery_worker   | /usr/local/lib/python3.12/site-packages/celery/platforms.py:829: SecurityWarning: You're running the worker with superuser privileges: this is
celery_worker   | absolutely not recommended!
celery_worker   |
celery_worker   | Please specify a different user using the --uid option.
celery_worker   |
celery_worker   | User information: uid=0 euid=0 gid=0 egid=0
celery_worker   |
celery_worker   |   warnings.warn(SecurityWarning(ROOT_DISCOURAGED.format(
celery_worker   |
celery_worker   |  -------------- celery@174e2895e6ed v5.3.4 (emerald-rush)
celery_worker   | --- ***** -----
celery_worker   | -- ******* ---- Linux-6.4.16-linuxkit-x86_64-with-glibc2.31 2023-10-17 16:57:42
celery_worker   | - *** --- * ---
celery_worker   | - ** ---------- [config]
celery_worker   | - ** ---------- .> app:         nerd_api:0x7fb160a7ed20
celery_worker   | - ** ---------- .> transport:   redis://redis:6379/0
celery_worker   | - ** ---------- .> results:     redis://redis:6379/0
celery_worker   | - *** --- * --- .> concurrency: 4 (prefork)
celery_worker   | -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
celery_worker   | --- ***** -----
celery_worker   |  -------------- [queues]
celery_worker   |                 .> celery           exchange=celery(direct) key=celery

"""
