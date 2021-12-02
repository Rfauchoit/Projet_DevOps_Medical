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
    data=patient.fetchInfirmier()  
    return patientcontroller.addPatient(data)

@app.route("/traitementPatient", methods=['POST', 'GET'])
def traitementPatient():
      data=request.form
      return patientcontroller.traitementPatient(patient, data)


@app.route("/traitementUpdate", methods=['POST', 'GET'])
def traitementUpdate():
      data=request.form
      return patientcontroller.traitementUpdate(patient, data)
  
@app.route("/updatePatient") 
def updatePatient():
    data=request.args
    return patientcontroller.updatePatient(patient, data)

@app.route("/displayPatient")
def affichage():
    return patientcontroller.fetch_patient(patient)



