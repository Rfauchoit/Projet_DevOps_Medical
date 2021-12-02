from flask import render_template

class deplacementController():
    def fetch_deplacement(self, deplacement):
        result = deplacement.fetchAll()
        return render_template("displayDeplacement.html", data= result)
