FROM python:3.10
RUN apt-get update && apt-get upgrade -y
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /app
# Копирует все файлы из нашего локального проекта в контейнер
ADD ./web_application /app
COPY poetry.lock pyproject.toml /
RUN pip3 install poetry

RUN poetry install