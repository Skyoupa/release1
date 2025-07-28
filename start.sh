#!/bin/bash

# 🚀 Script de démarrage Oupafamilly
# Usage: ./start.sh

echo "🎮 Démarrage de Oupafamilly Gaming Community"
echo "============================================"

# Couleurs pour les messages
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Fonction pour vérifier si une commande existe
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Vérification des prérequis
echo -e "${YELLOW}🔍 Vérification des prérequis...${NC}"

if ! command_exists python3; then
    echo -e "${RED}❌ Python 3 n'est pas installé${NC}"
    exit 1
fi

if ! command_exists node; then
    echo -e "${RED}❌ Node.js n'est pas installé${NC}"
    exit 1
fi

if ! command_exists yarn; then
    echo -e "${RED}❌ Yarn n'est pas installé${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Tous les prérequis sont installés${NC}"

# Vérification des fichiers de configuration
if [ ! -f "backend/.env" ]; then
    echo -e "${YELLOW}⚠️  Copie du fichier de configuration backend...${NC}"
    cp backend/.env.example backend/.env
    echo -e "${YELLOW}📝 Éditez backend/.env avec vos configurations${NC}"
fi

if [ ! -f "frontend/.env" ]; then
    echo -e "${YELLOW}⚠️  Copie du fichier de configuration frontend...${NC}"
    cp frontend/.env.example frontend/.env
fi

# Installation des dépendances si nécessaire
if [ ! -d "frontend/node_modules" ]; then
    echo -e "${YELLOW}📦 Installation des dépendances frontend...${NC}"
    cd frontend && yarn install && cd ..
fi

# Vérification MongoDB
echo -e "${YELLOW}🗄️  Vérification de MongoDB...${NC}"
if ! pgrep -x "mongod" > /dev/null; then
    echo -e "${RED}❌ MongoDB ne semble pas être en cours d'exécution${NC}"
    echo -e "${YELLOW}💡 Démarrez MongoDB avant de continuer${NC}"
    exit 1
fi

echo -e "${GREEN}✅ MongoDB est en cours d'exécution${NC}"

# Création de l'utilisateur admin si nécessaire
echo -e "${YELLOW}👤 Configuration de l'utilisateur administrateur...${NC}"
cd backend && python3 init_admin.py && cd ..

echo ""
echo -e "${GREEN}🎉 Configuration terminée !${NC}"
echo ""
echo -e "${YELLOW}📋 Pour démarrer l'application :${NC}"
echo ""
echo -e "${GREEN}Terminal 1 (Backend):${NC}"
echo "cd backend && uvicorn server:app --host 0.0.0.0 --port 8001 --reload"
echo ""
echo -e "${GREEN}Terminal 2 (Frontend):${NC}"
echo "cd frontend && yarn start"
echo ""
echo -e "${GREEN}🌐 URLs d'accès :${NC}"
echo "Frontend: http://localhost:3000"
echo "Backend API: http://localhost:8001"
echo "API Documentation: http://localhost:8001/docs"
echo ""
echo -e "${GREEN}👤 Connexion Admin par défaut :${NC}"
echo "Email: admin@oupafamilly.com"
echo "Mot de passe: Oupafamilly2024!"
echo ""
echo -e "${YELLOW}⚠️  N'oubliez pas de changer le mot de passe admin après la première connexion !${NC}"