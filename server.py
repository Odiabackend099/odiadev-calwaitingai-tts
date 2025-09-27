from flask import Flask, request, send_file, jsonify
import os
from TTS.api import TTS

app = Flask(__name__)

# Load a pretrained TTS model
model_name = TTS.list_models()[0]   # e.g., first available model
tts = TTS(model_name)

@app.route("/tts", methods=["POST"])
def tts_endpoint():
    try:
        data = request.get_json()
        text = data.get("text", "Hello from CallWaiting.ai")
        speaker = data.get("speaker", None)
        output_file = "output.wav"

        # Generate audio
        if speaker:
            tts.tts_to_file(text=text, file_path=output_file, speaker=speaker)
        else:
            tts.tts_to_file(text=text, file_path=output_file)

        return send_file(output_file, mimetype="audio/wav")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
