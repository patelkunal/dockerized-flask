FROM python:3.5.2
MAINTAINER Kunal Patel <patelkunal89@gmail.com>

RUN mkdir -p /opt/flasky-service

RUN apt-get update && apt-get install -y supervisor

COPY conf/flasky-supervisord.conf /etc/supervisor/conf.d/flasky-supervisord.conf

COPY requirements.txt /tmp/
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r /tmp/requirements.txt

COPY app /opt/flasky-service

EXPOSE 8000

WORKDIR /opt/flasky-service

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/flasky-supervisord.conf"]
