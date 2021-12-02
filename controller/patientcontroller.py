from flask import render_template
from werkzeug.utils import redirect
from controller.abstractController import abstractController

class patientController():
   
    def __init__(self):

        self.idpatient=None
        self.idadresse=None
   
        
    def read(self, patient):
        result = patient.read()
        return render_template("displayPatient.html", data = result)

   
    def create(self, data):
        return render_template("/addpatient.html", data=data)
    
    def treateCreate(self, patient, data):
        patient.create(data)
        return redirect("/")
    
    def update(self, patient,data):
        self.idpatient=data.get('idpatient') #permet de garder le idpatient pour le update
        dataPatient=patient.fetchAdressePatient(data)
        dataPatientAdd=patient.fetchInfirmierByIdPatient(dataPatient)
        if (dataPatientAdd!=None):
            dataPatient.update(dataPatientAdd)
        self.idadresse=dataPatient.get('idadresse')
        return render_template("updatePatient.html", data=dataPatient)
    
    def treateUpdate(self, patient, data):
        patient.update(data, self.idpatient, self.idadresse)
        return redirect("/displayPatient")
    
    def delete(self, patient, id):
        patient.delete(id)
        return redirect("/displayPatient")


