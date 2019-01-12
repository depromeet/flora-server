FROM ubuntu:18.04

# 필수 라이브러리 설치
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.6 python3.6-dev python3-pip

RUN ln -sfn /usr/bin/python3.6 /usr/bin/python3 && \
    ln -sfn /usr/bin/python3 /usr/bin/python && \
    ln -sfn /usr/bin/pip3 /usr/bin/pip

RUN apt-get install -y nginx \
    supervisor \
    locales \
    curl && \
    pip3 install --upgrade pip && \
    pip install uwsgi

RUN locale-gen ko_KR.UTF-8
    
# 프로젝트 구조 잡기

ENV PROJECT_ROOT /home/ubuntu
ENV PROJECT_SRC src
ENV PROJECT_UWSGI uwsgi

RUN mkdir ${PROJECT_ROOT}
WORKDIR ${PROJECT_ROOT}

RUN mkdir ${PROJECT_SRC} && \
    mkdir ${PROJECT_UWSGI}

# 웹 서버 설정
RUN echo "daemon off;" >> /etc/nginx/nginx.conf && \
    cd ${PROJECT_UWSGI}
COPY build/uwsgi_params build/uwsgi.ini ${PROJECT_UWSGI}/
COPY build/nginx.conf /etc/nginx/sites-available/default
COPY build/supervisor.conf /etc/supervisor/conf.d/
COPY build/start.sh ${PROJECT_ROOT}

RUN chmod +x ${PROJECT_ROOT}/start.sh

# 필요한 내용 복사 후 라이브러리 설치
COPY requirements.txt manage.py ${PROJECT_SRC}/

RUN cd ${PROJECT_SRC} && pip install -qq -r requirements.txt

# COPY config ${PROJECT_SRC}/config
# COPY utils ${PROJECT_SRC}/utils
# COPY apps ${PROJECT_SRC}/apps
# COPY api ${PROJECT_SRC}/api

ENTRYPOINT ["bash", "start.sh"]
CMD ["supervisord", "-n"]
