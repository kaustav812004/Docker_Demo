# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all files into /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Ensure Flask runs on all network interfaces
ENV FLASK_RUN_HOST=0.0.0.0

# Start Flask app
CMD ["python", "app.py"]
