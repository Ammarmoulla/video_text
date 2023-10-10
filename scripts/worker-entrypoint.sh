#!/bin/sh

# run a worker :)
celery -A core worker --loglevel=info --concurrency 1 -E

# celery -A core worker --loglevel=info --concurrency 1 -E -P gevent
