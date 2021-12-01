from flask import Flask, render_template
from werkzeug.utils import redirect
from model.patient import Patient
class PatientController():
     
#     def fetch_continent(self, continent):
#         result=continent.fetchAll()
#         return render_template("affichage.html", data= result)
    
    
#     def deleteById(self, continent, id):
#         continent.deleteById(id)
#         return redirect("/affichage")
    def traitementPatient(self, patient, data):
            patient.addPatient(data)
            return redirect("/")
 
    def addPatient(self):
        return render_template("addpatient.html")
    
#     def traitementContinent(self, continent, data):
#         print(data)
#         continent.addContinent(data)
#         return redirect("/affichage")
    
#     def traitementUpdate(self, continent, data):
#         print(data)
#         continent.update(data)
#         return redirect("/affichage")

#     def updateContinent(self, data):
#         return render_template("/updateContinent.html", data=data)