FROM python:3.5.2
MAINTAINER Kunal Patel <patelkunal89@gmail.com>

RUN mkdir -p /opt/app

RUN apt-get update && apt-get install -y vim nginx supervisor

RUN rm /etc/nginx/sites-enabled/default
COPY ./conf/flasky-nginx.conf /etc/nginx/sites-enabled/flasky-nginx.conf
RUN ln -sf /etc/nginx/sites-enabled/flasky-nginx.conf /etc/nginx/sites-available/flasky-nginx.conf

COPY ./conf/flasky-supervisord.conf /etc/supervisor/conf.d/flasky-supervisord.conf

COPY requirements.txt /tmp/
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r /tmp/requirements.txt

COPY ./app /opt/app

EXPOSE 80

WORKDIR /opt/app

# CMD ["/bin/bash"]
# CMD ["/usr/local/bin/gunicorn", "-b", ":8000", "hello:app"]
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/flasky-supervisord.conf"]
