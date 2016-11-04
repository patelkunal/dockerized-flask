FROM debian:jessie
MAINTAINER Kunal Patel <patelkunal89@gmail.com>

RUN apt-get update && apt-get install -y nginx supervisor

RUN rm /etc/nginx/sites-enabled/default
COPY ./conf/flasky-nginx.conf /etc/nginx/sites-enabled/flasky-nginx.conf
RUN ln -sf /etc/nginx/sites-enabled/flasky-nginx.conf /etc/nginx/sites-available/flasky-nginx.conf

COPY ./conf/flasky-supervisord.conf /etc/supervisor/conf.d/flasky-supervisord.conf

RUN mkdir -p /opt/flasky-www

COPY ./static /opt/flasky-www

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/flasky-supervisord.conf"]
