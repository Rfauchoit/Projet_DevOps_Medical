from flask import render_template
from werkzeug.utils import redirect

class patientController():
   
    def __init__(self):

        self.idpatient=None
        self.idadresse=None
   
        
    def fetch_patient(self, patient):
        result = patient.fetchAll()
        return render_template("displayPatient.html", data = result)

    def traitementPatient(self, patient, data):
            patient.addPatient(data)
            return redirect("/")
 

    def addPatient(self, data):
        return render_template("/addpatient.html", data=data)

    

    def traitementUpdatePatient(self, patient, data):
            patient.updatePatient(data, self.idpatient, self.idadresse)
            return redirect("/displayPatient")
    
   
     
 
        
    def updatePatient(self, patient,data):
        self.idpatient=data.get('idpatient') #permet de garder le idpatient pour le update
        dataPatient=patient.fetchAdressePatient(data)
        dataPatientAdd=patient.fetchInfirmierPatient(dataPatient)
        if (dataPatientAdd!=None):
            dataPatient.update(dataPatientAdd)
        self.idadresse=dataPatient.get('idadresse')
        return render_template("updatePatient.html", data=dataPatient)


    def deleteById(self, patient, id):
        patient.deleteById(id)
        return redirect("/displayPatient")


