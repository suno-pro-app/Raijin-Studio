from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Raijin Studio is LIVE 🔥"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
