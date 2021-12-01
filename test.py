from flask import render_template
from werkzeug.utils import redirect
from model.db import Db

class infirmierController():
    def fetch_patient(self, infirmier):
        result = infirmier.fetchAll() 
        return render_template("displayInfirmier.html", data= result)

