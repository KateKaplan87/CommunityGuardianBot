# main.py
import threading
import server  # stellt z. B. Flask bereit
import bot     # enthält den Discord-Bot

# Starte den Webserver in einem separaten Thread
threading.Thread(target=server.run).start()

# Starte den Discord-Bot
bot.run_discord_bot()


from server import keep_alive
from bot import run_discord_bot

if __name__ == '__main__':
    keep_alive()
    run_discord_bot()
