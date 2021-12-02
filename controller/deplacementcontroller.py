from flask import render_template
from werkzeug.utils import redirect

class deplacementController():
    def fetch_deplacement(self, deplacement):
        result = deplacement.fetchAll()
        return render_template("displayDeplacement.html", data= result)
    
        
    def addDeplacement(self):
        return render_template("addDeplacement.html")
    
    
    def traitementDeplacement(sef, deplacement, data):
        deplacement.addDeplacement(data)
        return redirect("/displayPatient")
    
    
    def updateDeplacement(self, deplacement, data):
        return render_template("updateDeplacement.html", data=data)


    def traitementUpdateDeplacement(self, patient, data):
        patient.updateDeplacement(data)
        return redirect("/displayPatient")
    
    def deleteById(self, deplacement, id):
        deplacement.deleteById(id)
        return redirect("/displayDeplacement")
    
    
