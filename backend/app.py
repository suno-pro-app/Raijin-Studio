from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Path sa frontend/index.html
    return send_file("../frontend/index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
@app.route("/generate", methods=["POST"])
def generate():
    # Placeholder: dito lalagay ang AI music generation
    return "🎵 Track generated! (placeholder)"
