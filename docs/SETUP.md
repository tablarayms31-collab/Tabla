# Guide d'Installation - IP-UGANC Portal

## 📌 Prérequis

- Docker & Docker Compose
- Git
- Un éditeur de code (VS Code, PHPStorm, etc.)
- Connexion Internet

## 🚀 Installation Rapide avec Docker

### 1. Cloner le dépôt

```bash
git clone https://github.com/tablarayms31-collab/Tabla.git
cd Tabla
```

### 2. Configurer les variables d'environnement

```bash
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

Modifiez les fichiers `.env` selon vos besoins.

### 3. Lancer les services Docker

```bash
docker-compose up -d
```

### 4. Initialiser la base de données

```bash
docker-compose exec backend php bin/migrate.php
```

### 5. Accéder à l'application

- **Frontend**: http://localhost:8501
- **API Backend**: http://localhost:8000
- **Base de données**: localhost:5432

## 🔧 Installation Manuelle

### Backend (PHP)

```bash
cd backend
cp .env.example .env

# Installer les dépendances
composer install

# Lancer le serveur
php -S localhost:8000 -t public
```

### Frontend (Streamlit)

```bash
cd frontend
cp .env.example .env

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app.py
```

### Base de Données (PostgreSQL)

```bash
# Créer la base de données
psql -U postgres -c "CREATE DATABASE ip_uganc;"

# Restaurer le schéma (à la création du projet)
psql -U postgres -d ip_uganc < database/schema.sql
```

## 🐳 Commandes Docker Utiles

```bash
# Démarrer les services
docker-compose up -d

# Arrêter les services
docker-compose down

# Voir les logs
docker-compose logs -f

# Exécuter une commande dans un conteneur
docker-compose exec backend php -v

# Reconstruire les images
docker-compose build
```

## 🧪 Tests

### Backend

```bash
cd backend
phpunit
```

### Frontend

```bash
cd frontend
pytest
```

## 📝 Commandes de Développement

### Code Formatting

```bash
# Backend (PHP)
cd backend
vendor/bin/php-cs-fixer fix src/

# Frontend (Python)
cd frontend
black .
flake8 .
```

### Linting

```bash
# Backend
cd backend
phpstan analyse src/

# Frontend
cd frontend
pylint .
```

## 🔒 Configuration de Sécurité

### Variables d'Environnement Sensibles

Assurez-vous de modifier ces variables en production:

- `JWT_SECRET` - Clé secrète JWT
- `ENCRYPTION_KEY` - Clé de chiffrement
- `DB_PASSWORD` - Mot de passe base de données
- `MAIL_PASSWORD` - Mot de passe email

### HTTPS en Production

Configurer SSL/TLS avec Let's Encrypt:

```bash
sudo apt-get install certbot python3-certbot-nginx
sudo certbot certonly --nginx -d your-domain.com
```

## 📞 Support

En cas de problème, consultez:
- [Documentation API](API.md)
- [Architecture](ARCHITECTURE.md)
- [Issues GitHub](https://github.com/tablarayms31-collab/Tabla/issues)

