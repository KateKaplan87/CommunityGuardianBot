import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("BOT_PREFIX", "!")

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # wichtig für Bots ab API v10

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot ist online als {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

def run_discord_bot():
    if not TOKEN:
        print("❌ Kein Token gefunden. Bitte DISCORD_TOKEN setzen.")
        return
    bot.run(TOKEN)
