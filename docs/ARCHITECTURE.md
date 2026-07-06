# Architecture - IP-UGANC Portal

## 📋 Vue d'ensemble architecturale

```
┌──────────────────────────────────────────────────────────────────────┐
│                    Frontend (Streamlit)                     │
│  Pages: Actualités, Calendrier, Espace Étudiant, etc.     │
└──────────────────────────────────────────────────┬──────────────────┘
                         │ HTTP/REST
                         ▼
┌──────────────────────────────────────────────────────────────────────┐
│                   Backend API (PHP)                         │
│  • Controllers (Request handling)                           │
│  • Services (Business logic)                                │
│  • Models (Data access)                                     │
│  • Middleware (Authentication, Validation)                  │
└──────────────────────────────────────────────────┬──────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────────┐
│                   PostgreSQL Database                       │
│  Tables: Users, Actualités, Calendrier, etc.               │
└──────────────────────────────────────────────────────────────────────┘
```

## 🔄 Communication

1. **Frontend** → Utilisateur interagit avec l'application Streamlit
2. **API REST** → Frontend envoie des requêtes HTTP au backend PHP
3. **Backend** → Traite les requêtes, valide les données
4. **Database** → Stocke et récupère les données
5. **Frontend** ← Affiche les résultats à l'utilisateur

## 📦 Structure des Composants

### Backend

```
api/
├── Controllers → Gèrent les requêtes HTTP
├── Services → Logique métier
├── Models → Interaction avec la BD
└── Middleware → Authentification, validation, CORS
```

### Frontend

```
app/
├── Pages → Pages principales
├── Components → Éléments réutilisables
└── Utils → Fonctions utilitaires (API client, helpers)
```

## 🔐 Sécurité

### Authentification
- JWT (JSON Web Tokens)
- Gestion des sessions côté backend
- Refresh tokens

### Validation
- Validation côté serveur obligatoire
- Validation côté client pour UX
- Protection CSRF
- Sanitization des entrées

### Protection
- HTTPS en production
- CORS configuré
- Rate limiting
- Protection XSS
- Protection injection SQL (requêtes paramétrées)

## 📊 Modèle de Données

### Tables Principales

- **users** - Utilisateurs (étudiants, enseignants, admins)
- **actualites** - Actualités et nouvelles
- **calendrier** - Événements académiques
- **inscriptions** - Inscriptions étudiantes
- **resultats** - Résultats académiques
- **ressources** - Ressources bibliothèque
- **offres_emploi** - Offres de recrutement
- **projets** - Projets internationaux
- **galerie** - Contenus multimédia

## 🚀 Déploiement

### Architecture de Déploiement

```
Ubuntu Server
├── Docker
│   ├── Backend (PHP-FPM)
│   ├── Frontend (Streamlit)
│   └── PostgreSQL
├── Nginx (Reverse Proxy)
└── SSL/TLS (HTTPS)
```

## ⚡ Performance

- **Cache** : Implémentation Redis (optionnel)
- **Compression** : Gzip pour les réponses
- **CDN** : Pour les assets statiques
- **Indexation** : Indexes BD pour requêtes fréquentes

## 🔄 Flux de Requête Typique

1. Utilisateur remplit un formulaire dans le frontend
2. Frontend valide les données côté client
3. Frontend envoie POST/PUT/GET à l'API backend
4. Backend middleware valide l'authentification (JWT)
5. Controller valide les paramètres
6. Service exécute la logique métier
7. Model interagit avec la base de données
8. Backend retourne une réponse JSON
9. Frontend traite la réponse et met à jour l'UI

