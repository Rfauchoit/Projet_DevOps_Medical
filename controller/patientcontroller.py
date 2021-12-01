from flask import render_template

class patientController():    
    def fetch_patient(self, patient):
        result = patient.fetchAll() 
        return render_template("displayPatient.html", data = result)
    