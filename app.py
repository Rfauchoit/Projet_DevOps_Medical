from flask import Flask, render_template, request
from model.patient import Patient
from controller.patientController import PatientController

app = Flask("/")


patient=Patient()
patientController = PatientController()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addPatient")
def addPatient():
    return patientController.addPatient()

@app.route("/traitementPatient", methods=['POST', 'GET'])
def traitementPatient():
      data=request.form
      print(data)
      return patientController.traitementPatient(patient, data)
    
    
    
