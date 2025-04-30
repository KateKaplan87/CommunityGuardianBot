import subprocess

subprocess.Popen(["python", "bot.py"])

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ CommunityGuardianBot läuft!"

def run():
    app.run(host="0.0.0.0", port=8080)

