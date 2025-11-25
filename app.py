from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello (Cruel) World!"

if __name__ == "__main__":
    # 0.0.0.0 kell Dockerhez, port 8080 a feladat szerint is jó
    app.run(host="0.0.0.0", port=8080)
