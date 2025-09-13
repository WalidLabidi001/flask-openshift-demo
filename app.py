from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello c'est ma premiere modification OpenShift Sandbox avec Flask!"

@app.route("/about")
def about():
    return "Ceci est un déploiement Flask via OpenShift S2I."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
