FROM python:3.11-slim

# Встановлення системних залежностей
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-cffi \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

# Встановлення робочої директорії
WORKDIR /app

# Копіювання файлів проекту
COPY . .

# Встановлення Python залежностей
RUN pip install --no-cache-dir -r requirements.txt

# Збірка статичних файлів
RUN python manage.py collectstatic --noinput

# Відкриття порту
EXPOSE 8000

# Команда запуску
CMD ["gunicorn", "meditation_app.wsgi:application", "--bind", "0.0.0.0:8000"] 