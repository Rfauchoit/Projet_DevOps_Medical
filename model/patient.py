from model.db import Db

class Patient(Db):
    def __init__(self):
        super().__init__()
    
    def fetchAll(self):
        self.cursor=self.getCursor()
        sqlp="SELECT nom, prenom, securite_sociale FROM patient"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchall()
        self.cursor.close()
        return rows
        
# patient=Patient()
# a=patient.fetchAll()
# print(a)