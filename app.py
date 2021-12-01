from flask import Flask, render_template
from controller.patientcontroller import patientController
from model.patient import Patient

app = Flask(__name__)
patient=Patient()
patientcontroller = patientController()



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/displayPatient")
def affichage():
    return patientcontroller.fetch_patient(patient)