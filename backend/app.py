from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Raijin Studio is LIVE 🔥</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # IMPORTANT
    app.run(host="0.0.0.0", port=port)
