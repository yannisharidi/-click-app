# Utilisez une image de Python existante comme image parente
FROM python:3.8-slim-buster

# Définir le répertoire de travail
WORKDIR /authentification

# Copier les fichiers du projet dans le conteneur
COPY . /authentification

# Installer les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8080
EXPOSE 8080

# Démarrer l'application
CMD ["python", "main.py"]