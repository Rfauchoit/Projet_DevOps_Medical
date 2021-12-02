from flask import Flask, render_template, request

from model.patient import Patient
from controller.patientcontroller import patientController
from controller.infirmiercontroller import infirmierController
from controller.deplacementcontroller import deplacementController
from model.infirmier import Infirmier
from model.deplacement import Deplacement


app = Flask(__name__)
deplacement = Deplacement()
deplacementcontroller = deplacementController()
infirmier = Infirmier()
infirmiercontroller = infirmierController()
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
  
@app.route("/addDeplacement")
def addDeplacement():
    return deplacementcontroller.addDeplacement()

@app.route("/traitementDeplacement", methods=['POST', 'GET'])
def traitementDeplacement():
      data=request.form
      return deplacementcontroller.traitementDeplacement(deplacement, data)


@app.route("/updatePatient")  
def updatePatient():
    data=request.args
    return patientcontroller.updatePatient(patient, data)

@app.route("/traitementUpdatePatient", methods=['POST', 'GET'])
def traitementUpdatePatient():
      data=request.form
      return patientcontroller.traitementUpdatePatient(patient, data)
  

@app.route("/updateDeplacement")  
def updateDeplacement():
    data=request.args
    return deplacementcontroller.updateDeplacement(data)

@app.route("/traitementUpdateDeplacement", methods=['POST', 'GET'])
def traitementUpdateDeplacement():
      data=request.form
      return deplacementcontroller.traitementUpdateDeplacement(deplacement, data)


@app.route("/displayPatient")
def affichagepatient():
    return patientcontroller.fetch_patient(patient)


@app.route("/displayInfirmier")
def affichageinfirmier():
    return infirmiercontroller.fetch_infirmier(infirmier)


@app.route("/displayDeplacement")
def affichagedeplacement():
    return deplacementcontroller.fetch_deplacement(deplacement)

@app.route('/delete/<int:id>', methods = ['GET', 'POST'])

def deletepatient(id):
    return patientcontroller.deleteById(patient, id)

@app.route('/delete/<int:id>', methods = ['GET', 'POST'])
def deleteinfirmier(id):
    return infirmiercontroller.deleteById(infirmier, id)


