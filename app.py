import psutil
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello (Cruel) DevOps World!"

@app.route("/info")
def info():
    return "App: Hello (Cruel) DevOps World – Verzio 1.0.0"

@app.route("/egeszseg")
def health_check_std():
    process = psutil.Process()
    memory_bytes = process.memory_info().rss  # RAM usage
    memory_mb = memory_bytes / (1024 * 1024)

    return jsonify({
        "status": "ok",
        "memory_mb": round(memory_mb, 2),
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
