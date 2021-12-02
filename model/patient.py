from model.db import Db

class Patient(Db):
    def __init__(self):
        super().__init__()
    
    def fetchAll(self):
        self.cursor=self.getCursor()
        sqlp=f"SELECT nom, prenom, securite_sociale, idpatient FROM patient"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchall()
        self.cursor.close()
        return rows 
    

    def fetchInfirmier(self):
        """[Methode qui permet de récuper nom, prénom, numéro_pro infirmer]

        Returns:
            [dict]: [nom, prenom, numero_pro]
        """
        self.cursor=self.getCursor()
        sqlp="SELECT nom, prenom, numero_pro FROM infirmier"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchall()
        self.cursor.close()
        return rows 
    
    def fetchInfirmierPatient(self, patientData):
        """[Methode qui permet de récuper numéro_pro infirmer]

        Returns:
            [dict]: [nom, prenom, numero_pro]
        """
        self.cursor=self.getCursor()
        sqlp=f"SELECT numero_pro FROM infirmier where idinfirmier='{patientData.get('infirmier_idinfirmier')}'" 
       
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchone()
        self.cursor.close()
        return rows 
    
    
    def fetchAdresse(self, patientData):
        """[Methode qui permet de récuper l'idadresse a partir du numéro/rue ille et cp]

         Args:
           patientData ([type]): [description]

        Returns:
             [int]: [le idadresse]
        """
     
        self.cursor=self.getCursor()
        sqlSelect=f"""SELECT idadresse FROM adresse WHERE adresse.numero='{patientData.get('numero')}'
        and  adresse.rue= '{patientData.get('rue')}'and adresse.cp='{patientData.get('cp')}' 
        and adresse.ville='{patientData.get('ville')}';"""
        self.cursor.execute(sqlSelect)
        rows=self.cursor.fetchone()
        self.cursor.close()
        if (type(rows).__name__!= "NoneType") :
            return rows.get('idadresse')
    
    
<<<<<<< HEAD
=======
    def fetchOneInfirmier(self, patientData):
        """[Methode qui permet de récuper l'id de l'infirmier à partir de son numéro pro]

        Args:
            patientData ([type]): [description]

        Returns:
            [int]: [le idadresse]
        """
        self.cursor=self.getCursor()
        sqlSelect=f"""SELECT idinfirmier FROM infirmier WHERE infirmier.numero_pro='{patientData.get('numero_pro')}';"""
        self.cursor.execute(sqlSelect)
        rows=self.cursor.fetchone()
        self.cursor.close()
        if (type(rows).__name__!= "NoneType") :
            return rows.get('idinfirmier')
    
    def fetchAdressePatient(self, patientData):
        """[cette methode sert à faire un select les infos du patient
           et son adresse dans la table adresse
        ]

        Args:
                patientData ([dict]): [les infos du patients]

        """
        self.cursor=self.getCursor()
        sqlp=f"""SELECT nom, prenom, securite_sociale, idpatient, naissance, sexe, 
            securite_sociale, rue, numero, ville, cp, adresse.idadresse, infirmier_idinfirmier FROM patient 
            left join adresse on patient.adresse_idadresse=adresse.idadresse WHERE idpatient='{patientData.get('idpatient')}'"""
          
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchone()
        self.cursor.close()
        return rows 
    

>>>>>>> develop
    def addPatient(self, patientData):
        """[cette methode sert à ajouter un patient dans la base medical, table patient]
        
        Args:
            patientData ([dict]): [les infos du patients]
        """
        id_infirmier=None
        id_adresse=None
        if type(patientData.get('numero_pro')).__name__!='NoneType':
             id_infirmier=self.fetchOneInfirmier(patientData)
            
        if type(patientData.get('numero')).__name__!= "NoneType" :
            id_adresse=self.fetchAdresse(patientData)
           
        self.cursor=self.getCursor()
        sql = """INSERT INTO patient (adresse_idadresse, infirmier_idinfirmier, 
              nom, prenom, naissance, sexe, securite_sociale)
              VALUES (%s, %s, %s, %s, %s, %s, %s);"""
        val = (id_adresse,id_infirmier, patientData.get('nom'),  patientData.get('prenom'), patientData.get('naissance'),  patientData.get('sexe'),   patientData.get('securite_sociale') )
        self.cursor.execute(sql, val)
        self.cursor.close()
<<<<<<< HEAD

        def updatePatient(self, patientData):
           """[cette methode sert à mettre à jour les informations d'un patient dans la table patient]
=======
>>>>>>> develop

         
<<<<<<< HEAD
           sql=f"""UPDATE continent SET adresse_idadresse='{patientData.get('numero')}',
           nom='{patientData.get('nom')}', prenom='{patientData.get('prenom')}', 
           naissance='{patientData.get('naissance')}', sexe='{patientData.get('sexe')}', 
           securite_sociale='{patientData.get('securite_sociale')}' where idpatient='{patientData.get('idpatient')}'""" 
           self.cursor.execute(sql) 
           self.cursor.close()
    
=======
    def updatePatient(self, patientData, idpatient, idadresse):
        """[cette methode sert à mettre à jour les informations d'un patient dans la table patient 
        et son adresse dans la table adresse]

        Args:
                patientData ([dict]): [les infos du patients]
                idpatient : identifiant patient à mettre à jour
                idadresse : id adresse correspondant à patient
        """
      
        id_infirmier=None
        if type(patientData.get('numero_pro')).__name__!='NoneType':
             id_infirmier=self.fetchOneInfirmier(patientData)
        self.cursor=self.getCursor()
        sqlp=f"""UPDATE patient SET nom='{patientData.get('nom')}', 
        prenom='{patientData.get('prenom')}',naissance='{patientData.get('naissance')}',
        sexe='{patientData.get('sexe')}', infirmier_idinfirmier='{id_infirmier}' where idpatient like '{idpatient}'"""
        
        sqla=f"""UPDATE adresse SET numero='{patientData.get('numero')}',
        rue='{patientData.get('rue')}', ville='{patientData.get('ville')}', 
        cp='{patientData.get('cp')}'where idadresse like '{idadresse}'""" 
        
        self.cursor.execute(sqlp) 
        self.cursor.execute(sqla) 
       
        self.cursor.close()
             
>>>>>>> develop

    

    def deleteById(self, id):
        self.cursor=self.getCursor()
        sql = f"DELETE FROM patient WHERE idpatient = {id}"
        self.cursor.execute(sql)
        self.cursor.close()

