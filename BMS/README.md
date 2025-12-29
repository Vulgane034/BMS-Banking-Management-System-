# BMS - Banking Management System

Ce projet est un système de supervision et de régulation macroéconomique prédictif destiné aux banques centrales.

## Installation

1.  **Prérequis :** Assurez-vous d'avoir Python 3.8 ou une version plus récente installée sur votre système.
2.  **Cloner le projet :** Clonez ce dépôt sur votre machine locale.
3.  **Installer les dépendances :** Naviguez jusqu'au répertoire `BMS(Banking Management System)` et exécutez la commande suivante pour installer les bibliothèques Python requises :
    ```bash
    pip install -r requirements.txt
    ```

## Lancement du Tableau de Bord

Pour lancer l'application et le tableau de bord interactif, exécutez la commande suivante depuis le répertoire `BMS(Banking Management System)` :

```bash
streamlit run dashboard/dashboard.py
```

Cette commande démarrera le serveur web Streamlit et ouvrira l'application dans votre navigateur.

## Exécuter le Pipeline en Ligne de Commande

Si vous ne souhaitez pas utiliser le tableau de bord, vous pouvez exécuter le pipeline directement depuis la ligne de commande à partir du répertoire `BMS(Banking Management System)` :

```bash
python main.py
```
Cette commande exécutera le pipeline avec les paramètres par défaut et affichera les résultats dans la console.
