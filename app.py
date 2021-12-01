from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addpat")
def addPatient():
    return render_template("addpatient.html")

@app.route("/addinf")
def addInfirmier():
    return render_template("addInfirmier.html")

@app.route("/adddep")
def addDeplacement():
    return render_template("addDeplacement.html")


@app.route("/delpa")
def deletePatient():
    return render_template("deletePatient.html")

@app.route("/delinf")
def deleteInfirmier():
    return render_template("deleteInfirmier.html")