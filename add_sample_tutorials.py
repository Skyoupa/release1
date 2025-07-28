#!/usr/bin/env python3
"""
Script pour ajouter des tutoriels d'exemple
"""

import asyncio
import sys
import os
sys.path.append('/app/backend')

from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import uuid
from pathlib import Path
from dotenv import load_dotenv

# Configuration de la base de données
ROOT_DIR = Path(__file__).parent / 'backend'
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

async def add_sample_tutorials():
    """Ajouter des tutoriels d'exemple"""
    try:
        print("📚 Ajout de tutoriels d'exemple...")
        
        # Récupérer l'admin
        admin = await db.users.find_one({"role": "admin"})
        if not admin:
            print("❌ Aucun admin trouvé")
            return False
        
        admin_id = admin["id"]
        
        # Tutoriels CS2
        cs2_tutorials = [
            {
                "id": str(uuid.uuid4()),
                "title": "Maîtriser l'économie de CS2",
                "description": "Apprenez à gérer l'économie d'équipe pour maximiser vos chances de victoire",
                "game": "cs2",
                "level": "intermediate",
                "content": """
## Comprendre l'économie de CS2

L'économie est l'un des aspects les plus cruciaux de Counter-Strike 2. Une bonne gestion économique peut faire la différence entre une victoire et une défaite.

### Concepts de base

- **Full buy**: Achat complet (fusil d'assault + armor + utilitaires)
- **Eco round**: Round économique avec achats minimaux
- **Force buy**: Achat forcé avec l'argent disponible

### Règles d'or

1. Ne jamais gaspiller l'argent inutilement
2. Coordonner les achats avec l'équipe
3. Savoir quand forcer et quand économiser
4. Prévoir les rounds suivants

### Stratégies avancées

- Analyse des rounds adverses
- Gestion des rounds de bonus
- Anticipation des achats ennemis
                """,
                "author_id": admin_id,
                "tags": ["économie", "stratégie", "équipe"],
                "is_published": True,
                "sort_order": 2,
                "image": "/images/tutorials/cs2_economy.jpg",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": str(uuid.uuid4()),
                "title": "Améliorer son aim sur CS2",
                "description": "Techniques et exercices pour développer une précision redoutable",
                "game": "cs2",
                "level": "beginner",
                "content": """
## Améliorer son aim sur CS2

Un bon aim est essentiel pour performer sur Counter-Strike 2. Voici un guide complet pour développer votre précision.

### Configuration de base

- **Sensibilité**: Trouvez votre sensibilité idéale
- **Crosshair**: Configurez un viseur adapté
- **FPS**: Maintenir un framerate stable
- **Matériel**: Souris et tapis appropriés

### Exercices d'entraînement

1. **Aim training maps**
   - aim_botz
   - training_aim_csgo2
   
2. **Routine quotidienne**
   - 15 minutes de warm-up
   - Exercices de tracking
   - Flick shots

### Techniques avancées

- Pre-aim des angles communs
- Counter-strafe pour l'accuracy
- Gestion du spray pattern
- Positionnement du crosshair
                """,
                "author_id": admin_id,
                "tags": ["aim", "entraînement", "précision"],
                "is_published": True,
                "sort_order": 1,
                "image": "/images/tutorials/cs2_aim_training.jpg",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        ]
        
        # Tutoriels LoL
        lol_tutorials = [
            {
                "id": str(uuid.uuid4()),
                "title": "Maîtriser le last-hit sur LoL",
                "description": "Techniques pour farmer efficacement et prendre l'avantage économique",
                "game": "lol",
                "level": "beginner",
                "content": """
## Maîtriser le last-hit sur League of Legends

Le last-hit (dernier coup) est la base du jeu sur LoL. C'est votre principale source d'or et d'expérience.

### Les bases du farm

- **Timing**: Attaquer au bon moment
- **Damage**: Connaître ses dégâts d'attaque
- **Animation**: Maîtriser l'animation d'attaque
- **Positioning**: Se placer correctement

### Techniques avancées

1. **Animation cancel**
2. **Freeze de lane**
3. **Wave management**
4. **Back timing**

### Objectifs de farm

- **10 min**: 70-80 CS
- **20 min**: 150-170 CS
- **30 min**: 220-250 CS

### Conseils pratiques

- Entraînement en pratique tool
- Focus sur la régularité
- Adapter selon le matchup
- Ne pas sacrifier la sécurité
                """,
                "author_id": admin_id,
                "tags": ["farm", "économie", "laning"],
                "is_published": True,
                "sort_order": 1,
                "image": "/images/tutorials/lol_lasthit.jpg",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        ]
        
        # Tutoriels WoW
        wow_tutorials = [
            {
                "id": str(uuid.uuid4()),
                "title": "Guide des classes WoW",
                "description": "Découvrez les différentes classes et leurs spécialisations",
                "game": "wow",
                "level": "beginner",
                "content": """
## Guide des classes World of Warcraft

WoW propose une grande variété de classes, chacune avec ses spécialisations uniques.

### Classes de mêlée

**Guerrier**
- Protection (Tank)
- Fureur (DPS)
- Armes (DPS)

**Paladin**
- Sacré (Heal)
- Protection (Tank)
- Vindicte (DPS)

### Classes à distance

**Mage**
- Arcane (DPS)
- Feu (DPS)
- Givre (DPS)

**Chasseur**
- Maîtrise des bêtes (DPS)
- Précision (DPS)
- Survie (DPS)

### Hybrides

**Druide**
- Équilibre (DPS caster)
- Sauvage (DPS mêlée/Tank)
- Restauration (Heal)
- Gardien (Tank)

### Conseils pour débutants

1. Testez plusieurs classes
2. Lisez les guides de classe
3. Rejoignez une guilde
4. Pratiquez en donjon
                """,
                "author_id": admin_id,
                "tags": ["classes", "débutant", "guide"],
                "is_published": True,
                "sort_order": 1,
                "image": "/images/tutorials/wow_classes.jpg",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        ]
        
        all_tutorials = cs2_tutorials + lol_tutorials + wow_tutorials
        
        # Insérer tous les tutoriels
        for tutorial in all_tutorials:
            await db.tutorials.insert_one(tutorial)
        
        print(f"✅ {len(all_tutorials)} tutoriels ajoutés avec succès")
        
        # Vérification
        total_tutorials = await db.tutorials.count_documents({})
        print(f"📊 Total tutoriels en base: {total_tutorials}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {str(e)}")
        return False
    finally:
        client.close()

if __name__ == "__main__":
    success = asyncio.run(add_sample_tutorials())
    exit(0 if success else 1)