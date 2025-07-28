# 🎮 Oupafamilly - Elite Gaming Community

Une plateforme communautaire multigaming moderne développée avec FastAPI et React, conçue pour rassembler les passionnés de jeux vidéo dans une ambiance conviviale et familiale.

## ✨ Fonctionnalités

### 🏆 Système de Tournois
- Tournois multi-jeux (CS2, LoL, WoW, SC2, Minecraft)
- Formats variés : Élimination, Bracket, Round Robin
- Gestion automatique des matchs et brackets
- Système de récompenses et prix

### 👥 Communauté Sociale
- Profils utilisateurs détaillés avec statistiques
- Système de commentaires et évaluations (1-5 étoiles)
- Chat multi-canaux par jeu
- Feed d'activité social en temps réel
- Messages privés entre membres

### 🎯 Système ELO & Classements
- Système ELO complet avec 8 tiers de classement
- Suivi des performances par jeu
- Historique détaillé des matchs
- Classements saisonniers

### 💰 Économie Virtuelle
- Système de monnaie virtuelle (coins)
- Marketplace d'items (avatars, badges, titres)
- Système XP et niveaux
- Achievements et défis communautaires

### 📚 Contenu Éducatif
- Tutoriels par jeu et niveau de difficulté
- Guides stratégiques professionnels
- Ressources d'apprentissage enrichies

### 🛠 Administration
- Dashboard admin complet
- Gestion des utilisateurs et contenu
- Outils de modération
- Analytics et monitoring

## 🚀 Technologies

**Backend**
- FastAPI (Python)
- MongoDB avec Motor (async)
- JWT Authentication
- Redis Cache
- Rate Limiting
- Structured Logging

**Frontend** 
- React 19
- React Router DOM
- Tailwind CSS
- Axios
- Context API

**Intégrations**
- Discord Bot
- Steam API
- Stripe (payments)
- OpenAI (AI features)

## 📦 Installation

### Prérequis
- Python 3.11+
- Node.js 18+
- MongoDB
- Redis (optionnel)

### Backend
```bash
cd backend
pip install -r requirements.txt
python init_admin.py  # Créer admin par défaut
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

### Frontend
```bash
cd frontend
yarn install
yarn start
```

### Configuration
Configurez les variables d'environnement dans `.env` :

**Backend (.env)**
```
MONGO_URL=mongodb://localhost:27017
DB_NAME=oupafamilly_db
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
DISCORD_BOT_TOKEN=your-discord-token
STEAM_API_KEY=your-steam-key
```

**Frontend (.env)**
```
REACT_APP_BACKEND_URL=http://localhost:8001
```

## 👤 Connexion Admin Par Défaut

```
Email: admin@oupafamilly.com
Mot de passe: Oupafamilly2024!
```

⚠️ **Changez ce mot de passe en production !**

## 📖 Utilisation

1. **Première connexion** : Utilisez les identifiants admin
2. **Configuration** : Complétez votre profil et configurez la communauté
3. **Contenu** : Ajoutez des tutoriels et créez des tournois
4. **Membres** : Invitez des joueurs à rejoindre la communauté

## 🎯 Jeux Supportés

- **Counter-Strike 2** : Tournois, tutoriels tactiques
- **League of Legends** : Équipes 5v5, guides de rôles
- **World of Warcraft** : PvP Arena, guides de classes
- **StarCraft II** : 1v1 et matchs d'équipe
- **Minecraft** : Serveurs communautaires

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez les [issues](../../issues) pour les améliorations prévues.

## 📄 Licence

Projet développé pour la communauté Oupafamilly.

---

*Développé avec ❤️ pour rassembler les gamers dans une ambiance familiale*