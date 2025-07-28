#!/usr/bin/env python3
"""
Script pour ajouter des tournois d'exemple
"""

import asyncio
import sys
import os
sys.path.append('/app/backend')

from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timedelta
import uuid
from pathlib import Path
from dotenv import load_dotenv

# Configuration de la base de données
ROOT_DIR = Path(__file__).parent / 'backend'
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

async def add_sample_tournaments():
    """Ajouter des tournois d'exemple"""
    try:
        print("🏆 Ajout de tournois d'exemple...")
        
        # Récupérer l'admin
        admin = await db.users.find_one({"role": "admin"})
        if not admin:
            print("❌ Aucun admin trouvé")
            return False
        
        admin_id = admin["id"]
        
        # Tournois d'exemple
        tournaments = [
            {
                "id": str(uuid.uuid4()),
                "title": "🎯 Tournoi CS2 Débutants",
                "description": """
Tournoi spécialement conçu pour les joueurs débutants et intermédiaires de Counter-Strike 2.

**Format:** Élimination simple
**Maps:** Dust2, Mirage, Inferno
**Règles:** Format BO1 puis BO3 en finale

Venez découvrir la compétition dans une ambiance détendue et familiale ! 
Tous les niveaux sont les bienvenus.
                """,
                "game": "cs2",
                "tournament_type": "elimination",
                "max_participants": 16,
                "entry_fee": 0.0,
                "prize_pool": 100.0,
                "status": "open",
                "registration_start": datetime.utcnow(),
                "registration_end": datetime.utcnow() + timedelta(days=7),
                "tournament_start": datetime.utcnow() + timedelta(days=10),
                "tournament_end": None,
                "rules": """
# Règlement du Tournoi CS2 Débutants

## Format
- Élimination simple
- BO1 jusqu'en demi-finale
- BO3 en finale

## Maps
- Dust2, Mirage, Inferno, Cache, Overpass

## Règles générales
1. Respect obligatoire entre tous les participants
2. Ponctualité exigée (5min de retard = défaite)
3. Screenshots des résultats obligatoires
4. Aucun cheat ou programme externe autorisé

## Prix
- 1er place: 50€
- 2ème place: 30€ 
- 3ème place: 20€
                """,
                "organizer_id": admin_id,
                "participants": [],
                "matches": [],
                "winner_id": None,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": str(uuid.uuid4()),
                "title": "⚔️ League of Legends Cup",
                "description": """
Tournoi League of Legends en équipes de 5 joueurs.

**Format:** Bracket double élimination
**Niveau:** Tous niveaux acceptés
**Récompenses:** Coins et badges exclusifs

Formez vos équipes et prouvez votre valeur sur la Faille !
                """,
                "game": "lol",
                "tournament_type": "bracket",
                "max_participants": 8,
                "entry_fee": 0.0,
                "prize_pool": 200.0,
                "status": "draft",
                "registration_start": datetime.utcnow() + timedelta(days=3),
                "registration_end": datetime.utcnow() + timedelta(days=14),
                "tournament_start": datetime.utcnow() + timedelta(days=17),
                "tournament_end": None,
                "rules": """
# Règlement LoL Cup

## Format d'équipe
- 5 joueurs par équipe
- 1 remplaçant autorisé

## Format de jeu
- Double élimination
- BO3 en finale
- BO1 le reste du temps

## Règles
1. Draft pick mode uniquement
2. Pause maximum 5 minutes par match
3. Remake autorisé si bug majeur
4. Comportement sportif obligatoire

## Récompenses
- Équipe gagnante: 200 coins chacun + badge
- Finaliste: 100 coins chacun
                """,
                "organizer_id": admin_id,
                "participants": [],
                "matches": [],
                "winner_id": None,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": str(uuid.uuid4()),
                "title": "🏰 Tournoi WoW PvP Arena",
                "description": """
Compétition PvP en arène 2v2 sur World of Warcraft.

**Format:** Round Robin puis Playoffs
**Niveau:** Expérimenté recommandé
**Saison:** Dragonflight S4

Montrez vos compétences PvP dans l'arène !
                """,
                "game": "wow",
                "tournament_type": "round_robin",
                "max_participants": 12,
                "entry_fee": 0.0,
                "prize_pool": 150.0,
                "status": "open",
                "registration_start": datetime.utcnow(),
                "registration_end": datetime.utcnow() + timedelta(days=5),
                "tournament_start": datetime.utcnow() + timedelta(days=8),
                "tournament_end": None,
                "rules": """
# Règlement Tournoi WoW PvP

## Format
- Arène 2v2
- Round Robin puis playoffs top 4
- BO3 en phases finales

## Restrictions
- Niveau maximum uniquement
- Équipement PvP autorisé
- Consommables PvP standard

## Règles de conduite
1. Fair-play obligatoire
2. Pas de toxicité en chat
3. Signaler les bugs majeurs
4. Stream/Record recommandé

## Prix
- Champion: 75€
- Vice-champion: 50€
- 3ème place: 25€
                """,
                "organizer_id": admin_id,
                "participants": [],
                "matches": [],
                "winner_id": None,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        ]
        
        # Insérer tous les tournois
        for tournament in tournaments:
            await db.tournaments.insert_one(tournament)
        
        print(f"✅ {len(tournaments)} tournois ajoutés avec succès")
        
        # Vérification
        total_tournaments = await db.tournaments.count_documents({})
        print(f"📊 Total tournois en base: {total_tournaments}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {str(e)}")
        return False
    finally:
        client.close()

if __name__ == "__main__":
    success = asyncio.run(add_sample_tournaments())
    exit(0 if success else 1)