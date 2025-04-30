import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
BOT_PREFIX = os.getenv('BOT_PREFIX', '!')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot ist eingeloggt als {bot.user}")

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("🏓 Pong!")

def run_discord_bot():
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("❌ Kein Token gefunden. Bitte DISCORD_TOKEN setzen.")
