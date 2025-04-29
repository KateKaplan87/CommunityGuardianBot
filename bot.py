import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("BOT_PREFIX", "!")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot ist online als {bot.user}")

# Beispielbefehl
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

def run_discord_bot():
    bot.run(TOKEN)
