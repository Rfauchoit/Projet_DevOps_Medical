from flask import render_template
from werkzeug.utils import redirect

class infirmierController():
    def fetch_infirmier(self, infirmier):
        result = infirmier.fetchAll() 
        return render_template("displayInfirmier.html", data= result)
    
    def deleteById(self, infirmier, id):
        infirmier.deleteById(id)
        return redirect("/displayInfirmier")
    
    
    def traitementUpdateInfirmier(self, infirmier, data):
        infirmier.updateinfirmier(data)
        return redirect("/displayInfirmier")
      
       
    def updateInfirmier(self,infirmier, data):
       
        dataInfirmier=dict(data)
        dataInfirmier.update(infirmier.fetchAdresseByID(data.get("idadresse")))
        print(dataInfirmier)
        return render_template("updateInfirmier.html", data=dataInfirmier)

