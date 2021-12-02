from model.db import Db

class Patient(Db):
    def __init__(self):
        super().__init__()
    
    def fetchAll(self):
        self.cursor=self.getCursor()
        sqlp="SELECT nom, prenom, securite_sociale, idpatient FROM patient"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchall()
        self.cursor.close()
        return rows 
    
    def fetchAdresse(self, patientData):
        # recuperer l'id de l'adresse si elle existe
        self.cursor=self.getCursor()
        sqlSelect=f"SELECT idadresse FROM adresse WHERE adresse.numero='{patientData.get('numero')}' and  adresse.rue= '{patientData.get('rue')}' and adresse.cp='{patientData.get('cp')}' and adresse.ville='{patientData.get('ville')}' ;"
        self.cursor.execute(sqlSelect)
        rows=self.cursor.fetchone()
        self.cursor.close()
        if (type(rows).__name__!= "NoneType") :
            return rows.get('idadresse')
    
    
    
<<<<<<< HEAD
=======

>>>>>>> develop
    def addPatient(self, patientData):
        """[cette methode sert à ajouter un patient dans la base medical, table patient]

        Args:
            patientData ([dict]): [les infos du patients]
        """
        id_adresse=None
        if (type(patientData.get('numero')).__name__!= "NoneType") :
            print(patientData.get('adresse_idadresse'))
            id_adresse=self.fetchAdresse(patientData)
                
        self.cursor=self.getCursor()
        sql = "INSERT INTO patient (adresse_idadresse, infirmier_idinfirmier, nom, prenom, naissance, sexe, securite_sociale) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (id_adresse,None, patientData.get('nom'),  patientData.get('prenom'), patientData.get('naissance'),  patientData.get('sexe'),   patientData.get('securite_sociale') )
        self.cursor.execute(sql, val)
        self.cursor.close()
<<<<<<< HEAD
   
   
        def updatePatient(self, patientData):
           """[cette methode sert à mettre à jour les informations d'un patient dans la table patient]

           Args:
                patientData ([dict]): [les infos du patients]
           """
           
         
           sql=f"""UPDATE continent SET adresse_idadresse='{patientData.get('numero')}',
           nom='{patientData.get('nom')}', prenom='{patientData.get('prenom')}', 
           naissance='{patientData.get('naissance')}', sexe='{patientData.get('sexe')}', 
           securite_sociale='{patientData.get('securite_sociale')}' where idpatient='{patientData.get('idpatient')}'""" 
           self.cursor.execute(sql) 
           self.cursor.close()
    
=======
    
    def deleteById(self, id):
        self.cursor=self.getCursor()
        sql = f"DELETE FROM patient WHERE idpatient = {id}"
        self.cursor.execute(sql)
        self.cursor.close()
>>>>>>> develop
