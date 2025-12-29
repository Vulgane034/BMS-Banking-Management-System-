# BMS Backend

Ce backend fournit l’API sécurisée, la logique métier, l’intégration Gemini, la collecte de données macroéconomiques en temps réel et la gestion des utilisateurs pour le Banking Management System (BMS).

## Architecture
- **FastAPI** (API REST, documentation auto)
- **Sécurité** : Authentification JWT, hashage des mots de passe, gestion des rôles
- **Services** :
  - Intégration Gemini (recommandations IA)
  - Collecte de données macroéconomiques (APIs publiques, upload manuel)
  - Parsing de rapports (PDF, Excel, CSV)
- **Base de données** : PostgreSQL (ou SQLite pour dev)

## Lancer le backend localement
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints principaux
- `/api/auth` : Authentification, inscription, gestion des utilisateurs
- `/api/data` : Collecte et accès aux données macroéconomiques
- `/api/recommendation` : Génération de recommandations IA (Gemini)
- `/api/upload` : Upload et parsing de rapports

## Sécurité
- Authentification JWT obligatoire pour toutes les routes sauf `/login` et `/register`
- Hashage des mots de passe (bcrypt)
- Rôles : admin, analyste, partenaire

---

© BEAC, BMS Project