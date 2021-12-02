from flask import render_template
from werkzeug.utils import redirect

class infirmierController():
    
    def read(self, infirmier):
        result = infirmier.read() 
        return render_template("displayInfirmier.html", data= result)
      
    def create(self):
        pass
    
    def createUpdate(self):
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
    

