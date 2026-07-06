# 🎓 GUIDE COMPLET DU PROJET IP-UGANC PORTAL
## De ZÉRO à Production - Explication Complète

---

# 📋 TABLE DES MATIÈRES
1. [Résumé de la structure créée](#structure-créée)
2. [Explication de chaque fichier](#explication-fichiers)
3. [Étapes restantes](#étapes-restantes)
4. [Comment travailler dans VS Code](#vs-code)
5. [Plan d'action détaillé](#plan-action)

---

# 🎯 RÉSUMÉ EXÉCUTIF

**Vous avez demandé:** Option 1 - Initialiser la structure complète
**Backend:** PHP pur (pas Laravel)
**Frontend:** Streamlit (Python)
**Base de données:** PostgreSQL
**Conteneurisation:** Docker

**J'ai créé:** Une structure complète et prête pour le développement

---

# 📁 STRUCTURE CRÉÉE

```
Tabla/ (votre dépôt GitHub)
│
├── 📄 README.md                    ← Documentation principale du projet
├── 📄 .gitignore                   ← Fichiers ignorés par Git
├── 📄 .env.example                 ← Variables d'environnement exemple
├── 🐳 docker-compose.yml           ← Configuration Docker
│
├── 📁 backend/                     ← API PHP
│   ├── 📁 config/
│   │   └── env.php                 ← Charger les variables d'env
│   ├── 📁 public/
│   │   └── index.php               ← Point d'entrée API (TRÈS IMPORTANT)
│   ├── 📄 .env.example             ← Config backend
│   ├── 📄 composer.json            ← Dépendances PHP
│   └── 📄 README.md                ← Doc backend
│
├── 📁 frontend/                    ← App Streamlit
│   ├── 📄 app.py                   ← Application principale
│   ├── 📄 config.py                ← Configuration globale
│   ├── 📄 requirements.txt          ← Dépendances Python
│   ├── 📄 .env.example             ← Config frontend
│   ├── 📄 README.md                ← Doc frontend
│   ├── 📁 pages/                   ← 8 pages de l'application
│   │   ├── actualites.py
│   │   ├── calendrier.py
│   │   ├── espace_etudiant.py
│   │   ├── bibliotheque.py
│   │   ├── recrutement.py
│   │   ├── projets.py
│   │   ├── galerie.py
│   │   └── contact.py
│   └── 📁 components/              ← Composants réutilisables
│       ├── __init__.py
│       ├── navbar.py
│       ├── footer.py
│       ├── sidebar.py
│       └── cards.py
│
├── 📁 docs/                        ← Documentation
│   ├── ARCHITECTURE.md             ← Vue d'ensemble technique
│   ├── SETUP.md                    ← Guide d'installation
│   └── GUIDE_COMPLET.md            ← Ce fichier!
│
└── 📁 scripts/
    └── init-db.sql                 ← Schéma base de données
```

---

# 📖 EXPLICATION DE CHAQUE FICHIER

## 🔴 NIVEAU 1: FICHIERS ESSENTIELS (À COMPRENDRE EN PREMIER)

### 1. `README.md` 📄 (Project Root)
**Qu'est-ce que c'est?**
- Documentation principale du projet
- Première chose que les gens voient sur GitHub
- Explique le projet, comment l'installer, comment l'utiliser

**Pourquoi l'avez-vous?**
- C'est standard sur GitHub
- Donne une vue d'ensemble du projet

**À faire dans VS Code:**
- Lisez-le pour comprendre le projet
- Ne le modifiez pas maintenant

---

### 2. `.gitignore` 🚫
**Qu'est-ce que c'est?**
- Liste des fichiers que Git **ignore** (ne met pas sur GitHub)
- Contient: `.env`, `node_modules/`, `__pycache__/`, etc.

**Pourquoi l'avez-vous?**
- Pour éviter de mettre vos mots de passe sur GitHub
- `.env` contient: DB_PASSWORD, JWT_SECRET, etc.

**À faire dans VS Code:**
- Vous n'avez rien à modifier
- C'est automatique

**Important:**
```
❌ NE METTEZ JAMAIS LE FICHIER .env SUR GITHUB
✅ Mettez UNIQUEMENT .env.example
```

---

### 3. `.env.example` 📋 (Project Root)
**Qu'est-ce que c'est?**
- Modèle des variables d'environnement pour tout le projet
- Montre QUELLES variables sont nécessaires (sans les vraies valeurs)

**À faire dans VS Code:**
```bash
# Étape 1: Dupliquez le fichier
cp .env.example .env

# Étape 2: Modifiez les valeurs dans .env
DB_PASSWORD=votre_mot_de_passe
JWT_SECRET=votre_secret_jwt
```

**Contenu:**
```
APP_NAME="IP-UGANC Portal"
DB_HOST=postgres
DB_PASSWORD=changeme    # À modifier!
API_URL=http://localhost:8000
```

---

### 4. `docker-compose.yml` 🐳
**Qu'est-ce que c'est?**
- Lance 3 services en même temps: PostgreSQL, Backend, Frontend
- Un fichier, une commande: tout démarre

**À faire dans VS Code:**
```bash
# C'est tout ce que vous devez faire:
docker-compose up -d
```

**Ce qu'il fait:**
1. Crée une base de données PostgreSQL
2. Lance le serveur PHP (Backend)
3. Lance l'app Streamlit (Frontend)

---

## 🟡 NIVEAU 2: BACKEND PHP

### 5. `backend/public/index.php` ⭐⭐⭐ **TRÈS IMPORTANT**
**Qu'est-ce que c'est?**
- Le point d'entrée de votre API
- CHAQUE requête HTTP passe par ce fichier
- C'est comme le "chef d'orchestre" de votre backend

**À faire dans VS Code:**

1. Ouvrez le fichier: `backend/public/index.php`
2. Vous verrez:
```php
switch ($path) {
    case 'health':
        // Retourne que l'API fonctionne
        
    case 'auth/login':
        // À implémenter
        
    case 'actualites':
        // À implémenter
}
```

3. **Chaque `case` est une route** que le frontend peut appeler

**Exemple actuel:**
```php
case 'actualites':
    if ($method === 'GET') {
        echo json_encode(['data' => [], 'message' => 'to be implemented']);
    }
```

**À faire prochainement:**
```php
case 'actualites':
    if ($method === 'GET') {
        // Récupérer les données de la BD
        // Retourner un JSON avec les actualités
        echo json_encode([
            'data' => [
                ['id' => 1, 'title' => 'Actualité 1'],
                ['id' => 2, 'title' => 'Actualité 2'],
            ]
        ]);
    }
```

---

### 6. `backend/config/env.php` ⚙️
**Qu'est-ce que c'est?**
- Charge les variables du fichier `.env` en mémoire
- Permet d'utiliser: `getenv('DB_HOST')`, etc.

**À faire dans VS Code:**
- Vous n'avez rien à faire ici
- C'est automatique

**Comment ça fonctionne:**
```php
// Dans index.php, au début:
require_once __DIR__ . '/../config/env.php';

// Partout dans le code, vous pouvez utiliser:
$db_host = getenv('DB_HOST');  // Récupère "postgres" du .env
```

---

### 7. `backend/.env.example` 📋
**Qu'est-ce que c'est?**
- Variables spécifiques au backend

**À faire dans VS Code:**
```bash
cp backend/.env.example backend/.env
# Modifiez les valeurs si nécessaire
```

---

### 8. `backend/composer.json` 📦
**Qu'est-ce que c'est?**
- Liste des dépendances PHP
- Comme `package.json` en Node.js

**À faire dans VS Code:**
```bash
cd backend
composer install  # Installe les dépendances (une seule fois)
```

**Contient:**
```json
{
  "require": {
    "php": ">=8.0",
    "firebase/php-jwt": "^6.4",  // Pour authentification JWT
    "vlucas/phpdotenv": "^5.5"   // Pour .env
  }
}
```

**Après `composer install`:**
- Un dossier `vendor/` est créé
- Il contient toutes les dépendances
- Vous ne touchez jamais `vendor/`
- Mettez-le dans `.gitignore` ✓ (déjà fait)

---

### 9. `backend/README.md` 📖
**Qu'est-ce que c'est?**
- Documentation du backend
- Comment l'installer, comment l'utiliser

**À faire dans VS Code:**
- Lisez-le pour comprendre
- Ne le modifiez pas maintenant

---

## 🟡 NIVEAU 2: FRONTEND STREAMLIT

### 10. `frontend/app.py` ⭐⭐⭐ **TRÈS IMPORTANT**
**Qu'est-ce que c'est?**
- L'application principale Streamlit
- Lance toute l'interface utilisateur
- La page d'accueil

**À faire dans VS Code:**
```bash
cd frontend
streamlit run app.py
# L'app s'ouvre sur http://localhost:8501
```

**Contenu:**
```python
import streamlit as st

st.title("🎓 Portail IP-UGANC")
st.markdown("Bienvenue...")

if st.button("Voir les actualités →"):
    st.switch_page("pages/actualites.py")  # Va à la page actualités
```

**À savoir:**
- Streamlit crée l'interface AUTOMATIQUEMENT
- Pas besoin d'HTML/CSS
- `st.title()` crée un titre
- `st.button()` crée un bouton
- `st.write()` affiche du texte

---

### 11. `frontend/config.py` ⚙️
**Qu'est-ce que c'est?**
- Configuration globale du frontend
- URL de l'API, paramètres Streamlit, liste des modules

**À faire dans VS Code:**
```python
API_CONFIG = {
    "base_url": "http://localhost:8000",  # URL du backend
    "api_version": "v1",
}

MODULES = [
    {"name": "Actualités", "icon": "📰", "page": "pages/actualites.py"},
    # Si vous en ajoutez une nouvelle page, l'ajouter ici
]
```

**Pourquoi c'est utile:**
- Pas besoin de changer l'URL partout dans le code
- Changez une fois dans `config.py`, ça change partout

---

### 12. `frontend/requirements.txt` 📦
**Qu'est-ce que c'est?**
- Liste des dépendances Python
- Comme `package.json` en Node.js

**À faire dans VS Code:**
```bash
cd frontend
pip install -r requirements.txt  # Installe tout en une commande
```

**Contient:**
```
streamlit==1.31.0       # Framework pour l'interface
requests==2.31.0        # Pour appeler l'API backend
python-dotenv==1.0.0    # Pour les variables d'environnement
pandas==2.1.3           # Pour manipuler les données
```

---

### 13. `frontend/.env.example` 📋
**Qu'est-ce que c'est?**
- Variables spécifiques au frontend

**À faire dans VS Code:**
```bash
cp frontend/.env.example frontend/.env
# Modifiez si nécessaire
```

---

### 14. `frontend/README.md` 📖
**Qu'est-ce que c'est?**
- Documentation du frontend

---

## 🟢 NIVEAU 3: PAGES FRONTEND (8 fichiers)

### 15-22. `frontend/pages/*.py` (8 fichiers)

| Fichier | But |
|---------|-----|
| `actualites.py` | Affiche les actualités de l'université |
| `calendrier.py` | Calendrier des événements académiques |
| `espace_etudiant.py` | Espace personnel de l'étudiant |
| `bibliotheque.py` | Ressources pédagogiques |
| `recrutement.py` | Offres d'emploi |
| `projets.py` | Projets internationaux |
| `galerie.py` | Galerie de photos/vidéos |
| `contact.py` | Formulaire de contact |

**À faire dans VS Code:**

**Exemple: actualites.py**
```python
import streamlit as st
import requests
from frontend.config import API_CONFIG

def main():
    st.title("📰 Actualités")
    
    # Appeler l'API backend
    response = requests.get(
        f"{API_CONFIG['base_url']}/api/{API_CONFIG['api_version']}/actualites"
    )
    
    if response.status_code == 200:
        data = response.json()
        for actualite in data['data']:
            st.write(actualite['title'])  # Afficher le titre

if __name__ == "__main__":
    main()
```

**Chaque page:**
1. Appelle une route du backend
2. Reçoit les données en JSON
3. Les affiche à l'écran

---

## 🟢 NIVEAU 3: COMPOSANTS FRONTEND (4 fichiers)

### 23. `frontend/components/__init__.py`
**Qu'est-ce que c'est?**
- Importe tous les composants
- Permet de faire: `from frontend.components import navbar`

---

### 24. `frontend/components/navbar.py`
**Qu'est-ce que c'est?**
- Barre de navigation
- Affiche le logo et les menus

**À faire dans VS Code:**
```python
def navbar():
    st.markdown("# 🎓 IP-UGANC")
    st.markdown("---")  # Ligne horizontale
```

---

### 25. `frontend/components/footer.py`
**Qu'est-ce que c'est?**
- Pied de page
- Coordonnées, copyright, date

---

### 26. `frontend/components/sidebar.py`
**Qu'est-ce que c'est?**
- Menu latéral
- Liens vers les autres pages

---

### 27. `frontend/components/cards.py`
**Qu'est-ce que c'est?**
- Cartes d'affichage réutilisables
- Pour afficher les actualités, événements, etc. de façon uniforme

---

## 🔵 NIVEAU 4: DOCUMENTATION & SCRIPTS

### 28. `docs/ARCHITECTURE.md`
Vue d'ensemble technique du projet

### 29. `docs/SETUP.md`
Guide d'installation

### 30. `scripts/init-db.sql`
Schéma SQL pour la base de données PostgreSQL

---

# ✅ RÉSUMÉ: FICHIERS CRÉÉS

| Catégorie | Nombre | État |
|-----------|--------|------|
| Config projet | 4 | ✅ Prêt |
| Backend | 5 | ✅ Structure, à implémenter |
| Frontend | 13 | ✅ Structure, à implémenter |
| Composants | 5 | ✅ Basiques, à améliorer |
| Docs | 3 | ✅ Prêt |
| Scripts | 1 | ✅ Prêt |
| **TOTAL** | **31 fichiers** | **✅ Prêt à développer** |

---

# 📅 ÉTAPES RESTANTES (ROADMAP)

## **PHASE 1: CONFIGURATION & INSTALLATION** ⏱️ 2-3 jours

### Étape 1: Configurer les fichiers .env
```bash
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Modifier les valeurs dans chaque .env
```

### Étape 2: Installer les dépendances
```bash
# Backend
cd backend
composer install

# Frontend
cd frontend
pip install -r requirements.txt
```

### Étape 3: Configurer PostgreSQL
```bash
# Créer la base de données
createdb ip_uganc

# Charger le schéma
psql ip_uganc < scripts/init-db.sql
```

### Étape 4: Lancer l'application
```bash
# Option A: Avec Docker (recommandé)
docker-compose up -d

# Option B: Manuellement
# Terminal 1: Backend
cd backend && php -S localhost:8000 -t public

# Terminal 2: Frontend
cd frontend && streamlit run app.py
```

### Étape 5: Vérifier que tout fonctionne
- Frontend: http://localhost:8501 ✅
- Backend: http://localhost:8000/api/v1/health ✅

---

## **PHASE 2: DÉVELOPPEMENT BACKEND** ⏱️ 2-3 semaines

### Étape 6: Implémenter la connexion à la BD
- Créer `backend/src/models/Database.php`
- Ajouter des fonctions pour récupérer/insérer des données

### Étape 7: Authentification (Login/Register)
- Route: `POST /api/v1/auth/login`
- Route: `POST /api/v1/auth/register`
- Générer des JWT tokens

### Étape 8-10: Routes CRUD principales
```
GET    /api/v1/actualites          (Liste)
POST   /api/v1/actualites          (Créer - Admin)
GET    /api/v1/actualites/{id}     (Détail)
PUT    /api/v1/actualites/{id}     (Modifier - Admin)
DELETE /api/v1/actualites/{id}     (Supprimer - Admin)

Même chose pour:
- /calendrier
- /bibliotheque
- /recrutement
- /projets
- /galerie
```

---

## **PHASE 3: DÉVELOPPEMENT FRONTEND** ⏱️ 2 semaines

### Étape 11: Connecter Frontend à Backend
- Les pages appelent les routes de l'API
- Affichent les données reçues

### Étape 12-14: Développer chaque page
- `actualites.py` - Affiche la liste
- `calendrier.py` - Affiche les événements
- (Et les 6 autres...)

### Étape 15: Authentification Frontend
- Formulaire de login
- Stocker le JWT token
- Envoyer le token dans les requêtes

---

## **PHASE 4: TESTS & DÉPLOIEMENT** ⏱️ 1-2 semaines

### Étape 16-17: Tests
- Tests unitaires (Backend)
- Tests d'intégration (Frontend + Backend)

### Étape 18: Déploiement
- Sur un serveur Ubuntu
- Avec Nginx
- Avec SSL/HTTPS

---

# 💻 COMMENT TRAVAILLER DANS VS CODE

## 1. OUVRIR LE PROJET
```bash
git clone https://github.com/tablarayms31-collab/Tabla.git
cd Tabla
code .  # Ouvre VS Code
```

## 2. STRUCTURE DANS VS CODE

L'Explorer (Ctrl + B) affichera:
```
Tabla/
├── backend/
├── frontend/
├── docs/
├── scripts/
└── ...
```

---

## 3. MODIFIER UN FICHIER

### Exemple: Ajouter une nouvelle actualité à la route

**Fichier:** `backend/public/index.php`

1. Cliquez sur le fichier dans l'Explorer
2. Trouvez le `case 'actualites':`
3. Modifiez le code:

```php
case 'actualites':
    if ($method === 'GET') {
        // Avant (temporaire):
        echo json_encode(['data' => [], 'message' => 'to be implemented']);
        
        // À faire: Récupérer les vraies données
        // $actualites = $db->query("SELECT * FROM actualites");
        // echo json_encode(['data' => $actualites]);
    }
```

4. Sauvegardez: `Ctrl + S`
5. Testez en accédant à: http://localhost:8000/api/v1/actualites

---

## 4. LANCER L'APPLICATION

### Avec Docker (Facile)
```bash
# Terminal VS Code (Ctrl + `)
docker-compose up -d

# Logs
docker-compose logs -f
```

### Sans Docker (Manuel)

**Terminal 1:**
```bash
cd backend
php -S localhost:8000 -t public
```

**Terminal 2:**
```bash
cd frontend
streamlit run app.py
```

---

## 5. ACCÉDER À L'APPLICATION

- Frontend: http://localhost:8501
- Backend: http://localhost:8000/api/v1/health
- Database: PostgreSQL sur localhost:5432

---

## 6. DÉBOGUER

### Backend (PHP)
```php
// Afficher des infos de débogage
var_dump($data);     // Affiche les contenus
echo json_encode(['debug' => $variable]);  // Pour l'API
```

### Frontend (Streamlit)
```python
# Afficher des infos
st.write(data)       # Affiche n'importe quoi
st.json(data)        # Affiche du JSON formaté
```

---

## 7. EXTENSIONS RECOMMANDÉES VS CODE

- PHP Intelephense (pour PHP)
- Python (pour Python)
- Streamlit (pour Streamlit)
- Thunder Client (pour tester l'API)
- GitLens (pour Git)

---

# 🎯 PLAN D'ACTION ÉTAPE PAR ÉTAPE

## **JOUR 1: Configuration**
- [ ] Copier `.env.example` → `.env` (3 fichiers)
- [ ] Modifier les valeurs dans `.env`
- [ ] Lancer Docker: `docker-compose up -d`
- [ ] Vérifier l'accès à Frontend et Backend

## **JOUR 2: Backend - Connexion BD**
- [ ] Créer `backend/src/models/Database.php`
- [ ] Implémenter la méthode `connect()`
- [ ] Tester avec une requête simple

## **JOUR 3: Backend - Routes**
- [ ] Implémenter `GET /api/v1/actualites`
- [ ] Tester avec cURL ou Postman

## **JOUR 4-5: Backend - CRUD complet**
- [ ] `POST /api/v1/actualites` (créer)
- [ ] `PUT /api/v1/actualites/{id}` (modifier)
- [ ] `DELETE /api/v1/actualites/{id}` (supprimer)

## **JOUR 6-7: Frontend - Actualités**
- [ ] Remplir `frontend/pages/actualites.py`
- [ ] Appeler l'API
- [ ] Afficher les données

## **JOUR 8-14: Frontend - Autres pages**
- [ ] Faire la même chose pour les 7 autres pages

## **JOUR 15+: Tests & Améliorations**
- [ ] Tests
- [ ] Déploiement

---

# ❓ FAQ

**Q: Faut-il faire tous les fichiers à la fois?**
A: Non! Commencez par les étapes 1-5 (configuration). Puis passez au backend, puis au frontend.

**Q: Quelle est la durée estimée?**
A: 6-8 semaines pour avoir une version 1.0 fonctionnelle

**Q: Comment apprendre le PHP/Streamlit?**
A: Il y a des ressources à la fin de ce document

---

# 📚 RESSOURCES

- [PHP Docs](https://www.php.net/manual/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [Docker Docs](https://docs.docker.com/)

---

✅ **Vous êtes prêt à commencer!** 🚀

Prochaines étapes:
1. Configurez les fichiers `.env`
2. Installez les dépendances
3. Lancez l'application
4. Commencez le développement

Besoin d'aide? Demandez-moi! 💪

