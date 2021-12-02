from model.db import Db

class Deplacement(Db):
    def __init__(self):
        super().__init__()
    
    def fetchAll(self):
        self.cursor=self.getCursor()
        sqlp=f"SELECT nom, date, cout FROM deplacement"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchall()
        self.cursor.close()
        return rows
    
    def fecthPatientBySecu(self, data):
        """[récupère le idPatient à partir du numéro sécu]

        Args:
            data (int): [numéro secu]
        return idpatient
        """
        self.cursor=self.getCursor()
        sqlp=f"SELECT idpatient FROM patient where securite_sociale='{data.get('securite_sociale')}'"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchone()
        self.cursor.close()
        return rows.get("idpatient")
     
    def addDeplacement(self, patientData):
        """[cette methode sert à ajouter un deplacement en fonction du numéro de secu d'un patient]

        Args:
            patientData ([dict]): [les infos du patients]
        """
       
        idPatient=None
        if type(patientData.get('securite_sociale')).__name__!='NoneType':
            idPatient=self.fecthPatientBySecu(patientData)
            
        self.cursor=self.getCursor()
        sql = """INSERT IGNORE INTO deplacement (patient_idpatient, date,cout)
              VALUES (%s, %s, %s);"""
        val = (idPatient,  patientData.get('date'), patientData.get('cout'))
        self.cursor.execute(sql, val)
        self.cursor.close()
