from flask import Flask
import threading
import bot  # das ist deine bot.py

app = Flask(__name__)

@app.route("/")
def home():
    return "CommunityGuardianBot is running!"

def run_bot():
    bot.run_bot()  # startet den Discord-Bot aus bot.py

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()  # startet den Bot parallel
    app.run(host="0.0.0.0", port=8080)        # hält Railway aktiv
