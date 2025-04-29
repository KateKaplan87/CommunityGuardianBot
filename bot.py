import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("BOT_PREFIX", "!")

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} ist online!")

def run_discord_bot():
    bot.run(TOKEN)
# Hier wird der Hauptbot-Code reinkommen
