import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # wichtig für Slash-Befehle

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("BOT_PREFIX", "!")

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot ist online: {bot.user} (ID: {bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

def run_bot():
    if not TOKEN:
        print("❌ Kein Token gefunden. Bitte DISCORD_TOKEN setzen.")
        return
    bot.run(TOKEN)
