# Используем базовый образ Python 3.12
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential

# Копируем файл requirements.txt
COPY requirements.txt /app/

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё содержимое проекта в контейнер
COPY . /app/

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Копируем скрипт запуска
COPY entrypoint.sh /app/

# Делаем скрипт запуска исполняемым
RUN chmod +x /app/entrypoint.sh

# Указываем точку входа
ENTRYPOINT ["/app/entrypoint.sh"]
