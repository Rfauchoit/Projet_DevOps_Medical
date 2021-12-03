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

#---------------------------------CRUD PATIENT------------------------------#
@app.route("/displayPatient")
def affichagepatient():
    return patientcontroller.read(patient)

@app.route("/addPatient")
def addPatient():
    data=patient.fetchInfirmier()  

    return patientcontroller.create(data)

@app.route("/traitementPatient", methods=['POST', 'GET'])
def traitementPatient():
      data=request.form
      return patientcontroller.treateCreate(patient, data)
  

@app.route("/updatePatient")  
def updatePatient():
    data=request.args
    return patientcontroller.update(patient, data)


@app.route("/traitementUpdatePatient", methods=['POST', 'GET'])
def traitementUpdatePatient():
      data=request.form
      return patientcontroller.treateUpdate(patient, data)


@app.route('/deletePatient/<int:id>', methods = ['GET', 'POST'])
def deletePatient(id):
    return patientcontroller.delete(patient, id)

#---------------------------------CRUD DEPLACEMENT------------------------------#
@app.route("/displayDeplacement")
def affichagedeplacement():
    return deplacementcontroller.read(deplacement)

@app.route("/addDeplacement")
def addDeplacement():
    return deplacementcontroller.create()

@app.route("/traitementDeplacement", methods=['POST', 'GET'])
def traitementDeplacement():
      data=request.form
      return deplacementcontroller.treateCreate(deplacement, data)


@app.route("/updateDeplacement")  
def updateDeplacement():
    data=request.args
    return deplacementcontroller.update(data)

@app.route("/traitementUpdateDeplacement", methods=['POST', 'GET'])
def traitementUpdateDeplacement():

      data=request.form
      return deplacementcontroller.treateUpdate(deplacement, data)
  
@app.route('/deleteDeplacement/<int:id>', methods = ['GET', 'POST'])
def deleteDeplacement(id):
    return deplacementcontroller.delete(deplacement, id)

#---------------------------------CRUD INFIRMIER------------------------------#

@app.route("/addInfirmier")
def addInfirmier():
    return render_template("/addInfirmier.html")

@app.route("/traitementInfirmier", methods=['POST', 'GET'])
def traitementInfirmier():
    data=request.form
    return infirmiercontroller.traitementInfirmier(infirmier, data)

@app.route("/updateInfirmier")  
def updateInfirmier():
    data=request.args
    return infirmiercontroller.update(infirmier, data)

@app.route("/traitementUpdateInfirmier", methods=['POST', 'GET'])
def traitementUpdateInfirmier():
      data=request.form
      return infirmiercontroller.treateUpdate(infirmier, data)

@app.route("/displayInfirmier")
def affichageinfirmier():
    return infirmiercontroller.read(infirmier)

@app.route('/deleteInfirmier/<int:id>', methods = ['GET', 'POST'])
def deleteInfirmier(id):
    return infirmiercontroller.delete(infirmier, id)



