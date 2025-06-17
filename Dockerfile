FROM python:3.12-slim

WORKDIR /opt/app
RUN apt-get update \
    && groupadd -r app-user && useradd -d /opt/app -r -g app-user app-user \
    && chown app-user:app-user -R /opt/app

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt gunicorn

COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

COPY src src

EXPOSE 8000

USER app-user
ENTRYPOINT ["./entrypoint.sh"]