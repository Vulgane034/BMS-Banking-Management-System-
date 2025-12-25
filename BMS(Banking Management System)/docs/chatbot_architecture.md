# Architecture du Chatbot Expert de la BMS

## 1. Objectif

L'objectif de ce chatbot est de fournir une interface conversationnelle pour explorer les données macroéconomiques de la CEMAC, générer des analyses basées sur des cadres stratégiques et offrir des recommandations qui tiennent compte des contraintes réglementaires.

## 2. Composants de l'Architecture

L'architecture du chatbot sera basée sur les composants suivants :

### a. Interface Utilisateur (UI)

- **Composant Streamlit :** Le chatbot sera intégré directement dans le tableau de bord Streamlit existant.
- **Zone de saisie de texte :** Pour que l'utilisateur puisse poser des questions en langage naturel.
- **Zone d'affichage de la conversation :** Pour afficher l'historique de la conversation entre l'utilisateur et le chatbot.

### b. Moteur de Traitement du Langage Naturel (NLP)

- **Bibliothèque de NLP :** Nous utiliserons une bibliothèque comme `spaCy` ou `NLTK` pour l'analyse de base du texte (tokenisation, reconnaissance d'entités nommées, analyse de l'intention).
- **Modèle de langage pré-entraîné (LLM) :** Pour une compréhension plus avancée du langage naturel et la génération de réponses, nous pourrions envisager d'utiliser un LLM plus petit et auto-hébergé (pour des raisons de confidentialité et de contrôle) ou d'utiliser une API de LLM si la confidentialité des données le permet.

### c. Module de Connaissances

Ce module sera responsable de la récupération des informations nécessaires pour répondre aux questions de l'utilisateur. Il sera composé de plusieurs sous-modules :

- **Accès aux Données du DataFrame :** Ce sous-module interrogera directement le DataFrame `pandas` contenant les données de la BEAC. Il pourra extraire des statistiques, des valeurs spécifiques et des séries temporelles.
- **Base de Connaissances Stratégiques :** Une base de connaissances (qui pourrait être un ensemble de documents structurés, une base de données ou même des invites codées en dur pour un LLM) contiendra des informations sur :
    - **Cadres d'analyse :** Définitions et méthodologies pour PESTEL et l'analyse des cinq forces de Porter.
    - **Réglementations :** Résumés et points clés de Bâle II et des réglementations de la COBAC.
- **Historique de la conversation :** Pour maintenir le contexte et permettre des conversations à plusieurs tours.

### d. Moteur de Génération de Réponses

- **Logique basée sur des règles :** Pour les questions simples et directes sur les données (par exemple, "Quelle est la valeur de X ?"), le chatbot utilisera des modèles de réponse prédéfinis.
- **Génération basée sur un LLM :** Pour les questions plus complexes nécessitant une analyse ou une interprétation, le chatbot enverra une invite au LLM qui inclura le contexte de la question, les données pertinentes du DataFrame et les informations de la base de connaissances stratégiques.

## 3. Flux de Travail

1.  **Entrée de l'utilisateur :** L'utilisateur saisit une question dans l'interface du chatbot.
2.  **Analyse NLP :** Le moteur de NLP analyse la question pour en extraire l'intention et les entités clés (par exemple, noms de colonnes, dates, cadres d'analyse).
3.  **Récupération des Connaissances :**
    - Si la question concerne directement les données, le module de connaissances interroge le DataFrame `pandas`.
    - Si la question implique une analyse stratégique ou réglementaire, le module de connaissances récupère les informations pertinentes de la base de connaissances.
4.  **Génération de l'Invite (si LLM utilisé) :** Pour les questions complexes, une invite est construite en combinant la question de l'utilisateur, les données récupérées et les connaissances contextuelles.
5.  **Génération de la Réponse :**
    - Le moteur de génération de réponses formule une réponse en utilisant soit une logique basée sur des règles, soit la sortie du LLM.
6.  **Sortie à l'utilisateur :** La réponse est affichée dans l'interface du chatbot.

## 4. Intégration avec le Pipeline Existant

- Le chatbot fonctionnera en parallèle avec le pipeline de prédiction existant.
- Les données chargées par `data_loader.py` et utilisées dans `pipeline.py` seront également accessibles par le chatbot.
- Le chatbot pourra, à l'avenir, déclencher des exécutions du pipeline de prédiction sur la base des demandes de l'utilisateur (par exemple, "Fais une prédiction pour la colonne X").

## 5. Exemples d'Interactions

- **Question sur les données :** "Quelle a été la tendance des 'Avoirs ext.' au cours des 5 dernières années ?"
- **Question d'analyse :** "Effectue une analyse PESTEL pour l'économie de la CEMAC."
- **Question réglementaire :** "Quelles sont les principales exigences de Bâle II en matière de fonds propres ?"
- **Question de recommandation :** "Sur la base des dernières prédictions, quelles mesures de politique monétaire devraient être envisagées, en tenant compte des réglementations de la COBAC ?"
