FROM python:3.11.2-slim-bullseye as build

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update \
    && apt-get install -qq -y  ffmpeg imagemagick  --no-install-recommends\
    && rm -rf /var/lib/apt/lists/*


WORKDIR /video_text
RUN useradd -ms /bin/bash celery && chown -R celery:celery /video_text

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./scripts/server-entrypoint.sh
RUN chmod +x ./scripts/worker-entrypoint.sh

USER celery
