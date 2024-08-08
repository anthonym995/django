# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variable to ensure output is sent straight to the terminal
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run migrations and custom command to add features, then start the Django server
CMD ["sh", "-c", "python manage.py migrate && python manage.py add_features && python manage.py creat_post && python manage.py runserver 0.0.0.0:8000"]
