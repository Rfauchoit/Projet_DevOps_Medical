from flask import Flask, render_template

class infirmierController():
    def fetch_patient(self, infirmier):
        result = infirmier.fetchAll() 
        return render_template("displayInfirmier.html", data= result)
