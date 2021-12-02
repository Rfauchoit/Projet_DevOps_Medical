from flask import render_template
from werkzeug.utils import redirect

class patientController():
   
    def __init__(self):
    #    self.setidpatient(i)
        self.idpatient=None
        self.idadresse=None
      
        
    # @property
    # def setidpatient(self):
    #     return self._idpatient
    
    # @setidpatient.setter
    # def setidpatient(self, id):
    #     self._idpatient=id
        
    def fetch_patient(self, patient):
        result = patient.fetchAll() 
        return render_template("displayPatient.html", data = result)

    def traitementPatient(self, patient, data):
            patient.addPatient(data)
            return redirect("/")
 
    def addPatient(self, data):
        return render_template("/addpatient.html", data=data)
    

    def traitementUpdate(self, patient, data):
            patient.updatePatient(data, self.idpatient, self.idadresse)
            return redirect("/")
 
        
    def updatePatient(self, patient,data):
        
        self.idpatient=data.get('idpatient') #permet de garder le idpatient pour le update
        data1=patient.fetchAdressePatient(data)
        data2=patient.fetchInfirmierPatient(data1)
        data1.update(data2)
        self.idadresse=data1.get('idadresse')
        return render_template("updatePatient.html", data=data1)