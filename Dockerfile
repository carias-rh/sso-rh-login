# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

ENV SECRET ''

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install oathtool -y

# Copy the application files to the container
COPY app.py .
COPY templates templates/

# Expose the container port
EXPOSE 5000

# Set the entrypoint command to run the Flask application
CMD ["python", "app.py"]
