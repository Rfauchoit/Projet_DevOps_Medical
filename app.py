from flask import Flask, render_template, request
from model.patient import Patient
from controller.patientcontroller import patientController

app = Flask(__name__)
patient=Patient()
patientcontroller = patientController()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addPatient")
def addPatient():
    return patientcontroller.addPatient()

@app.route("/traitementPatient", methods=['POST', 'GET'])
def traitementPatient():
      data=request.form
      print(data)
      return patientcontroller.traitementPatient(patient, data)
    
     
@app.route("/displayPatient")
def affichage():
    return patientcontroller.fetch_patient(patient)
