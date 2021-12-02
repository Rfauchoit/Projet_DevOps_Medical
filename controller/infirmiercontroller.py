from flask import render_template
from werkzeug.utils import redirect

class infirmierController():
    def __init__(self):
        self.idinfirmier=None
        self.idadresse=None
        
    def fetch_infirmier(self, infirmier):
        result = infirmier.fetchAll() 
        return render_template("displayInfirmier.html", data= result)
    
    def deleteById(self, infirmier, id):
        infirmier.deleteById(id)
        return redirect("/displayInfirmier")

    def traitementInfirmier(self, infirmier, data):
        infirmier.addInfirmier(data)
        return redirect("/displayInfirmier")

    def addInfirmier(self, data):
        return render_template("/addpatient.html", data=data)
