from flask import render_template
from werkzeug.utils import redirect

class deplacementController():
    def __init__(self):
        self.iddeplacement=None
    def fetch_deplacement(self, deplacement):
        result = deplacement.fetchAll()
        return render_template("displayDeplacement.html", data= result)
    
        
    def addDeplacement(self):
        return render_template("addDeplacement.html")
    
    
    def traitementDeplacement(sef, deplacement, data):
        deplacement.addDeplacement(data)
        return redirect("/displayPatient")
    
    
    def updateDeplacement(self, data):
        self.iddeplacement=data.get('iddeplacement')
        return render_template("updateDeplacement.html", data=data)


    def traitementUpdateDeplacement(self, deplacement, data):
        deplacement.updateDeplacement(data, self.iddeplacement)
        return redirect("/displayPatient")
    
    
    
