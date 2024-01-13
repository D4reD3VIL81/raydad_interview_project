# Use the official Python 3.9 image as the base
FROM python:3.9

# Install the PostgreSQL client
RUN apt-get update && \
    apt-get install -y postgresql-client

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY . /app/

# Install Poetry
RUN pip install poetry

RUN pip install --upgrade pip

ENV POETRY_HTTP_TIMEOUT=600
ENV PIP_TIMEOUT=600

# Install app dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

# Start the server using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "clinic_administrative_backend.wsgi"]