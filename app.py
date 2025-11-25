from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello (Cruel) DevOps World!"

@app.route("/info")
def info():
    return "App: Hello (Cruel) DevOps World – Verzio 1.0.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
