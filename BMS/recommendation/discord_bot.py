import discord
from discord.ext import commands
from recommendation import recommendation
import pandas as pd
import os

TOKEN = 'VOTRE_TOKEN_DISCORD_ICI'  # Remplacer par votre token

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

@bot.command()
async def reco(ctx):
    """Commande pour obtenir les recommandations macroéconomiques."""
    # Charger les scores simulés ou réels
    # Exemple : charger un fichier CSV de scores
    scores_path = os.path.join('..', 'evaluation', 'scores.csv')
    if os.path.exists(scores_path):
        df = pd.read_csv(scores_path, index_col=0)
        scores = df.to_dict(orient='index')
        recs = recommendation.generate_recommendations(scores)
        await ctx.send('\n'.join(recs))
    else:
        await ctx.send('Aucun score disponible. Veuillez exécuter l’évaluation des modèles.')

if __name__ == "__main__":
    bot.run(TOKEN)