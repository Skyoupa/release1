# 🔧 Documentation Développeur - Backend

## 📁 Structure du Backend

```
backend/
├── server.py           # Point d'entrée FastAPI principal
├── models.py           # Modèles Pydantic pour l'API
├── database.py         # Configuration MongoDB
├── auth.py            # Système d'authentification JWT
├── cache.py           # Gestion du cache Redis
├── validation.py      # Validateurs personnalisés
├── monitoring.py      # Logging et monitoring
├── achievements.py    # Système d'achievements
├── elo_system.py     # Calculs ELO et classements
├── steam_integration.py # Intégration API Steam
├── discord_bot.py    # Bot Discord (optionnel)
├── init_admin.py     # Script création admin
└── routes/           # Routes API organisées par domaine
    ├── auth.py       # Authentification utilisateurs
    ├── profiles.py   # Gestion des profils
    ├── tournaments.py # Système de tournois
    ├── teams.py      # Gestion des équipes
    ├── matches.py    # Matchs et résultats
    ├── content.py    # Tutoriels et contenu
    ├── community.py  # Interactions sociales
    ├── chat.py       # Système de chat
    ├── comments.py   # Commentaires et évaluations
    ├── currency.py   # Monnaie virtuelle
    ├── achievements.py # Achievements et défis
    ├── elo.py        # Classements ELO
    ├── betting.py    # Système de paris
    ├── admin.py      # Administration
    ├── analytics.py  # Statistiques
    ├── premium.py    # Fonctionnalités premium
    └── monitoring.py # Monitoring système
```

## 🗄️ Collections MongoDB

### Utilisateurs & Profils
- `users` - Comptes utilisateurs avec authentification
- `user_profiles` - Profils détaillés avec statistiques
- `user_inventory` - Inventaire d'items virtuels

### Gaming & Compétition
- `tournaments` - Tournois organisés
- `teams` - Équipes de joueurs
- `matches` - Matchs et résultats
- `elo_ratings` - Ratings ELO par utilisateur/jeu
- `elo_matches` - Historique des matchs ELO

### Contenu & Social
- `tutorials` - Guides et tutoriels
- `news` - Annonces et actualités
- `community_posts` - Posts communautaires
- `chat_messages` - Messages de chat
- `user_comments` - Commentaires sur profils
- `activity_feed` - Feed d'activité sociale

### Économie & Rewards
- `coin_transactions` - Transactions de monnaie virtuelle
- `marketplace_items` - Articles disponibles à l'achat
- `challenges` - Défis communautaires
- `user_challenges` - Progression des défis par utilisateur

## 🔐 Authentification

### JWT Tokens
- **Access Token**: Durée courte (15 min), pour les requêtes API
- **Refresh Token**: Durée longue (7 jours), pour renouveler l'access token

### Rôles Utilisateurs
- `admin` - Accès complet, gestion de la communauté
- `moderator` - Modération, gestion de contenu
- `member` - Utilisateur standard

### Permissions
```python
# Exemples de protection des routes
@router.post("/admin/users")
async def manage_users(current_user: User = Depends(is_admin)):
    pass

@router.put("/tournaments/{tournament_id}")
async def update_tournament(current_user: User = Depends(is_moderator_or_admin)):
    pass
```

## 📊 Système ELO

### Calcul des Ratings
- **Rating initial**: 1200 (Silver)
- **K-Factor**: 32 (ajustable selon l'expérience)
- **Minimum**: 800, **Maximum théorique**: ~2800

### Tiers de Classement
1. **Bronze**: 800-999
2. **Silver**: 1000-1199  
3. **Gold**: 1200-1399
4. **Platinum**: 1400-1599
5. **Diamond**: 1600-1799
6. **Master**: 1800-1999
7. **Grandmaster**: 2000-2199
8. **Challenger**: 2200+

## 🎮 Intégrations

### Steam API
- Vérification des profils Steam
- Statistiques de jeu CS2
- Authentification Steam (optionnel)

### Discord Bot
- Notifications de tournois
- Commandes de statistiques
- Intégration chat Discord

## 🔧 Configuration

### Variables d'Environnement Requises
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=oupafamilly_db
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
```

### Variables Optionnelles
```env
DISCORD_BOT_TOKEN=your-discord-token
STEAM_API_KEY=your-steam-key
STRIPE_SECRET_KEY=your-stripe-key
REDIS_URL=redis://localhost:6379/0
```

## 🚀 Démarrage Développement

```bash
# Installation dépendances
pip install -r requirements.txt

# Création admin
python init_admin.py

# Démarrage serveur de développement
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

## 📈 Performance

- **Cache Redis**: Utilisé pour les données fréquemment consultées
- **Index MongoDB**: Optimisés pour les requêtes principales
- **Rate Limiting**: Protection contre les abus
- **Pagination**: Limite de 100 résultats par défaut

## 🧪 Tests

Les endpoints principaux peuvent être testés via:
- **FastAPI Docs**: http://localhost:8001/docs
- **Health Check**: http://localhost:8001/api/health
- **API Status**: http://localhost:8001/api/