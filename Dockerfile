# Utilise une image Python légère
FROM python:3.10-slim

# Crée un dossier pour l'app
WORKDIR /app

# Copie les fichiers
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./
WORKDIR /app

# Création d’un dossier partagé pour les fichiers téléchargés
RUN mkdir -p /app/downloads

# Lance le script
CMD ["python", "start.py"]