# Architecture et Feuille de Route pour les Fonctionnalités Avancées

Ce document décrit l'architecture proposée et la feuille de route pour transformer le BMS en un outil avancé d'aide à la décision, intégrant un chatbot expert et des analyses stratégiques (PESTEL, Porter).

## Architecture Proposée

L'architecture s'articulera autour de trois composants principaux :

1.  **Interface Chatbot (Frontend) :**
    *   Une fenêtre de chat sera intégrée à l'interface Streamlit existante.
    *   Elle servira de point d'entrée unique pour que les analystes puissent poser des questions en langage naturel.

2.  **Orchestrateur d'IA (Backend) :**
    *   Ce composant sera le cœur du système, chargé d'interpréter les questions des utilisateurs et d'invoquer les outils appropriés.
    *   **Outils disponibles :**
        *   **Analyse de Données Quantitatives :** Interroge le `pipeline.py` pour obtenir des données chiffrées (inflation, PIB, etc.) provenant de sources structurées comme la Banque Mondiale.
        *   **Recherche Documentaire :** Interroge une base de données vectorielle pour trouver des informations qualitatives pertinentes dans des rapports, des articles de presse, etc.
    *   **Moteur de Synthèse :** Un Grand Modèle de Langage (LLM) sera utilisé pour agréger les informations des différents outils et générer une réponse cohérente, synthétique et contextualisée, en citant ses sources.

3.  **Base de Données Documentaire (Backend) :**
    *   **Collecte :** Des scripts de web scraping seront développés pour collecter automatiquement des documents (rapports de la BEAC, publications, etc.).
    *   **Stockage et Indexation :** Les documents seront stockés et transformés en "embeddings" à l'aide d'une base de données vectorielle (ex: ChromaDB, FAISS). Ce processus permet une recherche sémantique (basée sur le sens) extrêmement performante.

## Feuille de Route Détaillée

### Phase 1 : Recherche et Analyse Documentaire (Base pour PESTEL/Porter)

*   **Étape 1.1 : Web Scraping des Rapports de la BEAC :**
    *   Développer un script Python utilisant des bibliothèques comme `BeautifulSoup` et `requests` pour télécharger les publications du site `beac.int`.
*   **Étape 1.2 : Mise en Place de la Base de Données Vectorielle :**
    *   Intégrer une base de données vectorielle au projet.
    *   Développer le pipeline de traitement des documents : segmentation, création d'embeddings et indexation.
*   **Étape 1.3 : Création d'une API de Recherche :**
    *   Mettre en place une API simple (avec FastAPI par exemple) qui reçoit une requête en langage naturel et retourne les extraits de documents les plus pertinents de la base de données vectorielle.

### Phase 2 : Développement du Chatbot Expert

*   **Étape 2.1 : Intégration de l'Interface de Chat :**
    *   Ajouter un widget de chat à l'application Streamlit.
*   **Étape 2.2 : Développement de l'Orchestrateur d'IA :**
    *   Utiliser un framework comme LangChain ou LlamaIndex pour construire l'orchestrateur.
    *   Connecter les outils (API de données quantitatives et API de recherche documentaire) à l'orchestrateur.
*   **Étape 2.3 : Génération de Recommandations Basées sur le Contexte :**
    *   Concevoir et affiner des prompts pour le LLM afin qu'il puisse générer des analyses et des recommandations pertinentes, en fusionnant les informations des deux sources de données et en les alignant sur des cadres d'analyse comme PESTEL ou les 5 forces de Porter.
