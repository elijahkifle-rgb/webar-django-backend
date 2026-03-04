# Use a slim Python image
FROM python:3.12-slim
# force rebuild
# Set environment variables to avoid Python buffering and pyc files
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH="/app/src"

# Set work directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy project files
COPY . /app

# Use JSON format for CMD (recommended)
CMD ["gunicorn", "src.cfehome.cfehome.wsgi:application", "--bind", "0.0.0.0:8080"]