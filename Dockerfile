# Pull the base image
FROM python:3.10.4-slim-bullseye

# Set Environment variable
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project
COPY . .
