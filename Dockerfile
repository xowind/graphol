FROM think/plantuml:latest
MAINTAINER xowind

# basic flask environment
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk add --no-cache bash git nginx uwsgi uwsgi-python py2-pip ttf-freefont curl wqy-zenhei@testing \
	&& pip2 install --upgrade pip \
	&& pip2 install flask

# application folder
ENV APP_DIR /app

# app dir
RUN mkdir ${APP_DIR} \
	&& chown -R nginx:nginx ${APP_DIR} \
	&& chmod 777 /run/ -R \
	&& chmod 777 /root/ -R
VOLUME [${APP_DIR}]
WORKDIR ${APP_DIR}

# expose web server port
# only http, for ssl use reverse proxy
EXPOSE 80

# copy config files into filesystem
COPY nginx.conf /etc/nginx/nginx.conf
COPY app.ini /app.ini
COPY entrypoint.sh /entrypoint.sh
COPY app /app

# exectute start up script
ENTRYPOINT ["/entrypoint.sh"]
