from flask import Flask, request, send_file, jsonify
import os
import tempfile
import subprocess

app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def tts_endpoint():
    try:
        data = request.get_json()
        text = data.get("text", "Hello from CallWaiting.ai")
        speaker = data.get("speaker", None)
        
        # For now, create a simple text file response
        # This will be replaced with actual TTS once we get it working
        output_file = "output.txt"
        
        with open(output_file, "w") as f:
            f.write(f"TTS Request: {text}\n")
            f.write(f"Speaker: {speaker or 'default'}\n")
            f.write(f"Status: TTS service starting up...\n")
        
        return send_file(output_file, mimetype="text/plain")
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "running",
        "message": "CallWaiting.ai TTS API is starting up",
        "version": "1.0.0"
    })

if __name__ == "__main__":
    print("🚀 Starting CallWaiting.ai TTS API...")
    print("📡 API will be available at: http://localhost:8000")
    print("🔍 Health check: http://localhost:8000/health")
    print("🎤 TTS endpoint: POST http://localhost:8000/tts")
    app.run(host="0.0.0.0", port=8000, debug=True)