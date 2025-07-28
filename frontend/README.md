# 🎨 Documentation Développeur - Frontend

## 📁 Structure du Frontend

```
frontend/
├── public/               # Fichiers statiques
│   ├── index.html       # Template HTML principal
│   ├── manifest.json    # Manifeste PWA
│   ├── sw.js           # Service Worker
│   └── images/         # Images et assets
├── src/
│   ├── index.js        # Point d'entrée React
│   ├── App.js          # Composant principal
│   ├── App.css         # Styles globaux
│   ├── index.css       # Styles de base + Tailwind
│   ├── components/     # Composants réutilisables
│   ├── pages/         # Pages de l'application
│   ├── contexts/      # Contextes React (Auth, Theme)
│   ├── utils/         # Utilitaires et helpers
│   └── data/          # Données statiques
├── package.json        # Dépendances et scripts
├── tailwind.config.js  # Configuration Tailwind CSS
├── craco.config.js     # Configuration build
└── postcss.config.js   # Configuration PostCSS
```

## 🧩 Composants Principaux

### Layout & Navigation
- `Header.js` - Navigation principale avec authentification
- `Footer.js` - Pied de page avec liens utiles

### Authentification
- `AuthModal.js` - Modal de connexion/inscription
- `AuthContext.js` - Gestion de l'état d'authentification

### Gaming & Tournois
- `TournamentCard.js` - Affichage des tournois
- `TournamentBracket.js` - Visualisation des brackets
- `TeamManagement.js` - Gestion des équipes

### Social & Communauté
- `ProfilMembre.js` - Profils utilisateurs détaillés
- `NotificationCenter.js` - Centre de notifications
- `Chat.js` - Interface de chat temps réel

### Administration
- `AdminDashboard.js` - Tableau de bord admin
- `AdminUsers.js` - Gestion des utilisateurs
- `AdminContent.js` - Gestion du contenu

## 📱 Pages de l'Application

### Pages Publiques
- `/` - **Accueil** - Présentation de la communauté
- `/tournois` - **Tournois** - Liste des compétitions
- `/tutoriels` - **Tutoriels** - Guides par jeu
- `/communaute` - **Communauté** - Interactions sociales
- `/a-propos` - **À Propos** - Information sur la plateforme

### Pages Utilisateur
- `/profil` - **Mon Profil** - Gestion du compte personnel
- `/profil/:memberId` - **Profil Membre** - Profil d'un autre utilisateur

### Pages Admin
- `/admin` - **Dashboard Admin** - Vue d'ensemble
- `/admin/users` - **Gestion Utilisateurs**
- `/admin/tournaments` - **Gestion Tournois**
- `/admin/content` - **Gestion Contenu**

## 🎨 Système de Design

### Tailwind CSS
Configuration personnalisée avec palette de couleurs gaming :

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#6366f1',    // Indigo principal
        secondary: '#8b5cf6',  // Violet secondaire
        accent: '#06b6d4',     // Cyan accent
        gaming: {
          dark: '#0f172a',     // Bleu très sombre
          gray: '#1e293b',     // Gris gaming
          gold: '#fbbf24',     // Or pour récompenses
        }
      }
    }
  }
}
```

### Thème Sombre
Interface optimisée pour les gamers avec thème sombre par défaut.

## 🔗 Gestion d'État

### Contextes React

#### AuthContext
```javascript
const { user, login, logout, isLoading } = useAuth();
```
- Gestion de l'authentification utilisateur
- Stockage du token JWT
- Auto-refresh des tokens

#### ThemeContext
```javascript
const { theme, toggleTheme } = useTheme();
```
- Basculement thème clair/sombre
- Persistance des préférences

## 🌐 Communication API

### Configuration Axios
```javascript
// utils/api.js
const API_BASE_URL = process.env.REACT_APP_BACKEND_URL;

const api = axios.create({
  baseURL: `${API_BASE_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
});
```

### Endpoints Principaux
- `GET /tournaments` - Liste des tournois
- `GET /content/tutorials` - Tutoriels disponibles
- `POST /auth/login` - Connexion utilisateur
- `GET /profiles/:userId` - Profil utilisateur

## 📱 Responsive Design

### Breakpoints Tailwind
- `sm:` - 640px+ (Mobile large)
- `md:` - 768px+ (Tablette)
- `lg:` - 1024px+ (Desktop)
- `xl:` - 1280px+ (Large desktop)

### Composants Adaptatifs
Tous les composants sont conçus pour fonctionner sur mobile, tablette et desktop.

## ⚡ Performance

### Optimisations Appliquées
- **Code Splitting** - Chargement par routes
- **Lazy Loading** - Composants et images
- **Memoization** - React.memo pour composants lourds
- **Service Worker** - Cache des assets statiques

### Bundle Size
Cible: < 500KB gzipped pour le bundle principal

## 🚀 Scripts Disponibles

```bash
# Développement
yarn start          # Démarrage serveur dev (port 3000)

# Production
yarn build          # Build optimisé pour production
yarn serve          # Servir le build en local

# Qualité Code
yarn lint           # Linting avec ESLint
yarn format         # Formatage avec Prettier

# Tests
yarn test           # Tests unitaires avec Jest
```

## 🔧 Configuration

### Variables d'Environnement
```env
# .env
REACT_APP_BACKEND_URL=http://localhost:8001
REACT_APP_ENV=development
```

### Build Production
```bash
yarn build
# Génère le dossier build/ prêt pour déploiement
```

## 🎮 Fonctionnalités Gaming

### Interface Utilisateur Gaming
- Couleurs et design adaptés aux gamers
- Animations fluides et réactives
- Icônes et visuels gaming

### Temps Réel
- Notifications en temps réel
- Mise à jour des scores en direct
- Chat temps réel (WebSocket ready)

## 🧪 Testing

### Tests Recommandés
- Tests unitaires pour les utilitaires
- Tests d'intégration pour les composants
- Tests E2E pour les parcours utilisateur critiques

### Outils de Test
- **Jest** - Tests unitaires
- **React Testing Library** - Tests composants
- **Cypress** - Tests E2E (recommandé)