# 🚀 Guide d'Installation - Oupafamilly

## 📋 Prérequis

- **Python 3.11+** 
- **Node.js 18+** avec yarn
- **MongoDB** (local ou distant)
- **Git**

## ⚡ Installation Rapide

### 1. Cloner le Repository
```bash
git clone https://github.com/votre-username/oupafamilly.git
cd oupafamilly
```

### 2. Configuration Backend
```bash
cd backend

# Copier et configurer les variables d'environnement
cp .env.example .env
# Éditez .env avec vos configurations

# Installer les dépendances Python
pip install -r requirements.txt

# Créer l'utilisateur administrateur
python init_admin.py
```

### 3. Configuration Frontend
```bash
cd ../frontend

# Copier et configurer les variables d'environnement
cp .env.example .env
# Éditez .env si nécessaire

# Installer les dépendances Node.js
yarn install
```

## 🏃‍♂️ Démarrage

### Option 1: Démarrage Manuel

**Terminal 1 - Backend:**
```bash
cd backend
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
yarn start
```

### Option 2: Avec Docker (si disponible)
```bash
docker-compose up -d
```

## 🔧 Configuration

### Base de Données
1. Assurez-vous que MongoDB fonctionne
2. L'application créera automatiquement les collections nécessaires
3. Un utilisateur admin sera créé automatiquement

### Variables d'Environnement

**Backend (.env):**
- `MONGO_URL`: URL de connexion MongoDB
- `SECRET_KEY`: Clé secrète pour l'application
- `JWT_SECRET_KEY`: Clé pour les tokens JWT

**Frontend (.env):**
- `REACT_APP_BACKEND_URL`: URL du backend API

## 👤 Premier Connexion

```
URL: http://localhost:3000
Email: admin@oupafamilly.com
Mot de passe: Oupafamilly2024!
```

**⚠️ IMPORTANT:** Changez le mot de passe admin après la première connexion !

## 🎯 Fonctionnalités Disponibles

Une fois installé, vous aurez accès à :
- ✅ Système de tournois complet
- ✅ Profils utilisateurs et communauté
- ✅ Tutoriels et guides par jeu
- ✅ Système ELO et classements
- ✅ Chat et interactions sociales
- ✅ Dashboard d'administration

## 🔍 Vérification de l'Installation

1. **Backend API**: http://localhost:8001/api/health
2. **Frontend**: http://localhost:3000
3. **API Docs**: http://localhost:8001/docs

## 🚨 Résolution de Problèmes

### Backend ne démarre pas
- Vérifiez que MongoDB est en cours d'exécution
- Vérifiez les variables d'environnement dans `.env`
- Vérifiez les logs d'erreur dans le terminal

### Frontend ne charge pas
- Vérifiez que le backend est démarré
- Vérifiez `REACT_APP_BACKEND_URL` dans `.env`
- Videz le cache du navigateur

### Base de données vide
```bash
cd backend
python init_admin.py  # Recrée l'admin si nécessaire
```

## 📞 Support

Si vous rencontrez des problèmes, vérifiez :
1. Les prérequis sont installés
2. Les services (MongoDB) fonctionnent
3. Les ports 3000 et 8001 sont libres
4. Les fichiers `.env` sont correctement configurés