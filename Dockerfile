# Image Python
FROM python:3.11

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers du projet dans le conteneur
COPY . /app

RUN pip install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
# Installation les dépendances du projet
RUN pip install -r requirements.txt

# Exécutez l'application lorsque le conteneur démarre
CMD ["python", "src/main.py"]
