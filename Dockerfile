# Python image
FROM python:3.11

# Working directory in the container
WORKDIR /app

# Copy project files to container
COPY . /app

RUN pip install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
# Installation of project dependencies
RUN pip install -r requirements.txt

# Run the application when the container starts up
CMD ["python", "src/main.py"]
