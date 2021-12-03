from flask import render_template
from werkzeug.utils import redirect
from controller.abstractController import abstractController


class deplacementController():
    def __init__(self):
        self.iddeplacement=None
        
    def read(self, deplacement):
        result = deplacement.read()
        return render_template("displayDeplacement.html", data= result)
    
        
    def create(self):
        return render_template("addDeplacement.html")
    
    
    def treateCreate(sef, deplacement, data):
        deplacement.create(data)
        return redirect("/displayDeplacement")
    
    
    def update(self, data):
        self.iddeplacement=data.get('iddeplacement')
        return render_template("updateDeplacement.html", data=data)


    def treateUpdate(self, deplacement, data):
        deplacement.update(data, self.iddeplacement)
        return redirect("/displayDeplacement")
    
    def delete(self, deplacement, id):
        deplacement.delete(id)
        return redirect("/displayDeplacement")
    
    
