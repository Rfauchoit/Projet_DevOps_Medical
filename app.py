from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/inscription")
def add():
    return render_template("inscription.html")