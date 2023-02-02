# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Expose the API port
EXPOSE 8000

# Command to run when the container starts
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
