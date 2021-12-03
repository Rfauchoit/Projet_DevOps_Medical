from flask import render_template
from werkzeug.utils import redirect
from controller.abstractController import abstractController
class infirmierController(abstractController):

    def __init__(self):
        self.idinfirmier=None
        self.idadresse=None
        
  
    def read(self, infirmier):
        result = infirmier.read() 
        return render_template("displayInfirmier.html", data= result)
      
    def create(self):
        pass
    
    def treateCreate(self):
        pass
     
    def update(self,infirmier, data):
       
        dataInfirmier=dict(data)
        dataInfirmier.update(infirmier.fetchAdresseByID(data.get("idadresse")))
        print(dataInfirmier)
        return render_template("updateInfirmier.html", data=dataInfirmier)
    
    def treateUpdate(self, infirmier, data):
        infirmier.update(data)
        return redirect("/displayInfirmier")

    def delete(self, infirmier, id):
        infirmier.delete(id)
        return redirect("/displayInfirmier")
    
    def traitementInfirmier(self, infirmier, data):
        infirmier.addInfirmier(data)
        return redirect("/displayInfirmier")

    def addInfirmier(self, data):
        return render_template("/addpatient.html", data=data)

