FROM python:3.11.2-slim-bullseye as build

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update \
    && apt-get install -qq -y build-essential xvfb xdg-utils wget ffmpeg libpq-dev vim libmagick++-dev fonts-liberation sox bc --no-install-recommends\
    && apt-get clean

## ImageMagicK Installation ##
RUN mkdir -p /tmp/distr && \
    cd /tmp/distr && \
    wget https://download.imagemagick.org/ImageMagick/download/releases/ImageMagick-7.0.11-2.tar.xz && \
    tar xvf ImageMagick-7.0.11-2.tar.xz && \
    cd ImageMagick-7.0.11-2 && \
    ./configure --enable-shared=yes --disable-static --without-perl && \
    make && \
    make install && \
    ldconfig /usr/local/lib && \
    cd /tmp && \
    rm -rf distr

WORKDIR /video_text

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "sh", "start.sh" ]