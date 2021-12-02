from flask import render_template
from werkzeug.utils import redirect

class infirmierController():
    def fetch_infirmier(self, infirmier):
        result = infirmier.fetchAll() 
        return render_template("displayInfirmier.html", data= result)
    
    def deleteById(self, infirmier, id):
        infirmier.deleteById(id)
        return redirect("/displayInfirmier")
