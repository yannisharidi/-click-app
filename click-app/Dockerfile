# Utiliser l'image Nginx comme base
FROM nginx

# Copier le fichier HTML et le CSS dans le dossier de travail de Nginx
COPY index.html /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/

# Exposer le port 80 pour que Nginx puisse écouter les connexions entrantes
EXPOSE 80