# Odiadev CallWaiting.ai TTS

🚀 Production-ready TTS API powered by [Coqui TTS](https://github.com/coqui-ai/TTS).  
Deployed with Flask + Docker.

### Run locally
```bash
pip install -r requirements.txt
python3 server.py
```

### Run with Docker

```bash
docker build -t odiadev-tts .
docker run -p 8000:8000 odiadev-tts
```

### Example request

```bash
curl -X POST http://localhost:8000/tts \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world"}' --output output.wav
```
