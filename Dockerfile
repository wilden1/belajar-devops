FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy keperluan dulu (untuk speed up build)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file kod
COPY . .

# Beritahu port (optional tapi bagus)
EXPOSE 5000

# Jalankan app
CMD ["python", "app.py"]
