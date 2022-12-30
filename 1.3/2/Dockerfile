# Использовать официальный образ родительского образа / слепка.
FROM python:3.10
# set work directory
WORKDIR .
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .
# запускаем миграции
RUN python3 manage.py migrate
# Выполнить команду внутри контейнера
CMD python3 manage.py runserver 0.0.0.0:8000