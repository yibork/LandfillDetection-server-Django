# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8001 available to the world outside this container
EXPOSE 8001

# Define environment variable for Postgres service
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# Install PostgreSQL
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

# Run Postgres (customize this part with your own postgres setup scripts)
RUN service postgresql start && \
    su - postgres -c "psql -c \"CREATE USER $POSTGRES_USER WITH PASSWORD '$POSTGRES_PASSWORD';\"" && \
    su - postgres -c "createdb -O $POSTGRES_USER $POSTGRES_DB"

# Run migrations and start server as the last step
CMD service postgresql start && \
    sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8001"
