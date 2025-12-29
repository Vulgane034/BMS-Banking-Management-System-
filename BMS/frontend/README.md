# BMS Frontend

Ce frontend propose une interface moderne, modulaire et institutionnelle pour le Banking Management System (BMS).

## Architecture
- **React** (Vite ou Create React App)
- **TailwindCSS** pour le design
- **Pages** : LandingPage, Dashboard, Analyse Prédictive, Alertes, Recommandations IA, Simulation de Politiques, Gouvernance, Login
- **Composants** : Navbar, Sidebar, Footer, AlertBanner, RecommendationCard, CountryRiskMap, etc.
- **API** : intégration avec le backend BMS pour les recommandations, alertes, etc.

## Recommandation IA avec Gemini CLI
La page "Recommandations IA" interroge une API backend qui utilise Gemini CLI pour générer dynamiquement des recommandations économiques. Le backend doit exposer une route `/api/gemini-recommendation` qui appelle Gemini CLI et retourne les résultats au frontend.

## Lancer le frontend localement
```bash
cd frontend
npm install
npm run dev
```

## UX/UI
- Responsive, institutionnel (BEAC), navigation claire
- Sécurité : accès dashboard réservé (authentification)
- Intégration fluide des modules IA/backend

## Dépendances principales
- react, react-router-dom, tailwindcss, axios