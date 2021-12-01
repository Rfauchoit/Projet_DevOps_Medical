from flask import Flask, render_template, request

from model.patient import Patient
from controller.patientcontroller import patientController
from controller.infirmiercontroller import infirmierController
from model.infirmier import Infirmier


app = Flask(__name__)
infirmier = Infirmier()
infirmiercontroller = infirmierController()
patient=Patient()
patientcontroller = patientController()

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

@app.route("/displayInfirmier")
def affichage():
    return infirmiercontroller.fetch_infirmier(infirmier)
