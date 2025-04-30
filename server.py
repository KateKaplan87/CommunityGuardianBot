from flask import Flask
import threading

#import bot  # das ist deine bot.py



app = Flask('')


@app.route("/")
def home():
    return "CommunityGuardianBot is running!"

def run_discord_bot():
    if TOKEN:
       bot.run(TOKEN)

if __name__ == "__main__":
    threading.Thread(target=run_discord_bot).start()  # startet den Bot parallel
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
