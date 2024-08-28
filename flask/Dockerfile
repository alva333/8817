FROM python:3.12-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y apt-transport-https wget gnupg2 && \
    wget -qO - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    . /etc/os-release && echo "deb http://apt.postgresql.org/pub/repos/apt/ ${VERSION_CODENAME}-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    apt-get update && \
    apt-get install -y postgresql-client-13

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app app
COPY tests tests
COPY application.py .

EXPOSE 5000

CMD [ "python", "application.py"]