import numpy as np
import soundfile as sf
import io
from flask import send_file

@app.route("/generate", methods=["POST"])
def generate():
    # gumawa ng simpleng tone (music placeholder)
    sample_rate = 44100
    duration = 2  # seconds
    t = np.linspace(0, duration, int(sample_rate * duration))
    audio = 0.3 * np.sin(2 * np.pi * 440 * t)  # A note

    # save sa memory
    buffer = io.BytesIO()
    sf.write(buffer, audio, sample_rate, format="WAV")
    buffer.seek(0)

    return send_file(buffer, mimetype="audio/wav", download_name="track.wav")
