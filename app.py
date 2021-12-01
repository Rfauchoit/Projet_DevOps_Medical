from flask import Flask, render_template, request
<<<<<<< HEAD
from werkzeug.utils import redirect
from controller.infirmiercontroller import InfirmierController
from model.infirmier import Infirmier, infirmier
=======
from model.patient import Patient
from controller.patientcontroller import patientController
>>>>>>> develop

infirmier = Infirmier()
InfirmierController = InfirmierController()
app = Flask(__name__)
patient=Patient()
patientcontroller = patientController()


# @app.route("/")
# def hello():
#     return render_template("index.html")

# @app.route("/add")
# def add():
#     return render_template("formulaire.html")

# @app.route("/traitement", methods = ['POST', 'GET'])
# def traitement():
#     data = request.form
#     print(data)
#     return redirect('/')

@app.route("/displayinfirmier")
def affichage():
    return InfirmierController.fetch_infirmier(infirmier)

# @app.route('/delete/<int:id>')
# def delete(id):
#     return continentController.deleteById(continent, id)

# @app.route('/addContinent')
# def addContinent():
#     return continentController.addContinent()

# @app.route('/traitementContinent', methods=['POST','GET'])
# def traitementContinent():
#     data = request.form
#     return continentController.traitementContinent(continent, data)

# @app.route('/updateContinent', methods=['POST','GET'])
# def updateContinent():
#     data = request.args
#     return continentController.updateContinent(data)

<<<<<<< HEAD
# @app.route('traitementUpdate', methods=['POST','GET'])
# def traitementUpdate():
#     data = request.form
#     return continentController.traitementUpdate(continent, data)
=======
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
>>>>>>> develop
