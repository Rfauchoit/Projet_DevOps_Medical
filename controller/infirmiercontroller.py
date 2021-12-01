from flask import render_template

class infirmierController():
    def fetch_infirmier(self, infirmier):
        result = infirmier.fetchAll() 
        return render_template("displayInfirmier.html", data= result)
