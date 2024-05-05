# Используем базовый образ Python
FROM python:3.9

# Устанавливаем переменную окружения PYTHONUNBUFFERED на 1
# Это гарантирует, что вывод будет направлен прямо в терминал без буферизации,
# что полезно при просмотре логов или отладке
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости при помощи pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . /app/

# Запускаем сервер Django при помощи команды "python manage.py runserver"
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
