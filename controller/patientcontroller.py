from flask import render_template
from werkzeug.utils import redirect

class patientController():
    def fetch_patient(self, patient):
        result = patient.fetchAll() 
        return render_template("displayPatient.html", data = result)

    def traitementPatient(self, patient, data):
            patient.addPatient(data)
            return redirect("/")
 
    def addPatient(self):
        return render_template("addpatient.html")
    

    
    def traitementUpdate(self, patient, data):
            patient.addPatient(data)
            return redirect("/")
 
    def updatePatient(self):
        return render_template("updatepatient.html")

    def deleteById(self, patient, id):
        patient.deleteById(id)
        return redirect("/displayPatient")

