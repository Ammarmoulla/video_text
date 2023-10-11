#!/bin/sh

# run a worker :)

celery -A core worker --loglevel=info --concurrency 4 -E

# celery -A core worker --loglevel=info --concurrency 4 -E -P gevent
