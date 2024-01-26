# Use a base image for amd64
FROM python:3.9-slim

WORKDIR /app

# Copy your application files
COPY . /app/
COPY /tmp/data /tmp/data
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=http_server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Expose port 8080
EXPOSE 8080

# Command to run on container start
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
