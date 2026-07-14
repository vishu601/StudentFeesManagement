# 1. Base image set karo (Python ka light version)
FROM python:3.10-slim

# 2. Environment variables set karo taaki Python sahi se behave kare container mein
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Container ke andar working directory set karo
WORKDIR /app

# 4. System dependencies install karo (Pillow aur PostgreSQL binary ke liye)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. requirements.txt copy karo aur dependencies install karo
# (Yeh pehle isliye kar rahe hain taaki agar code badle, toh install dobara na karna pade)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Apne project ka baki saara code copy karo
COPY . /app/

# 7. Django server start karne ki command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
