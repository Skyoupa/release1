#!/usr/bin/env python3
"""
Test direct de la route tournaments
"""

import asyncio
import sys
import os
sys.path.append('/app/backend')

from motor.motor_asyncio import AsyncIOMotorClient
from pathlib import Path
from dotenv import load_dotenv

# Configuration de la base de données
ROOT_DIR = Path(__file__).parent / 'backend'
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

async def test_tournaments_endpoint():
    """Test direct de l'endpoint tournaments"""
    try:
        print("🧪 Test de l'endpoint tournaments...")
        
        # Test direct database
        tournaments_data = await db.tournaments.find({}).to_list(10)
        print(f"📊 Nombre de tournois trouvés: {len(tournaments_data)}")
        
        if tournaments_data:
            first_tournament = tournaments_data[0]
            print(f"📋 Premier tournoi: {first_tournament.get('title', 'Sans titre')}")
            print(f"🎮 Jeu: {first_tournament.get('game', 'N/A')}")
            print(f"📅 Status: {first_tournament.get('status', 'N/A')}")
            
            # Vérifier la structure
            print("🔍 Structure du premier tournoi:")
            for key, value in first_tournament.items():
                print(f"  {key}: {type(value).__name__}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {str(e)}")
        return False
    finally:
        client.close()

if __name__ == "__main__":
    success = asyncio.run(test_tournaments_endpoint())
    exit(0 if success else 1)