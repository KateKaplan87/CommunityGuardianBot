from flask import Flask
import threading

import bot  # das ist deine bot.py



app = Flask('')


@app.route("/")
def home():
    return "CommunityGuardianBot is running!"

def run_bot():
    bot.run_discord_bot()  # startet den Discord-Bot aus bot.py

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()  # startet den Bot parallel
    app.run(host="0.0.0.0", port=8080)        # hält Railway aktiv

@app.route('/')
def home():
    return "Bot is running!"

def keep_alive():
    thread = threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080))
    thread.start()

# Final bereinigte Version
def start():
    print("Remote-Version des Servers läuft")
