from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Suno Pro backend running!"

@app.route("/generate", methods=["POST"])
def generate():
    # Placeholder: dito lalagay ang AI music generation code
    return "Track generated!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
