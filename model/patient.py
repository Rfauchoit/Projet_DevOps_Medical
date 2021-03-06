from os import error

from mysql.connector.errors import InternalError
from model.db import Db

class Patient(Db):
    def __init__(self):
        super().__init__()
    
    #---------------------CRUD METHOD------------------------------------------------------------------------------#
    def read(self):
        self.cursor=self.getCursor()
        sqlp="SELECT nom, prenom, securite_sociale, idpatient FROM patient"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchall()
        self.cursor.close()
        return rows 

    def create(self, patientData):
        """[cette methode sert à ajouter un patient dans la base medical, table patient]

        Args:
            patientData ([dict]): [les infos du patients]
        """
        id_adresse=None

        if type(patientData.get('numero_pro')).__name__!='NoneType':
             id_infirmier=self.fetchOneInfirmier(patientData)
            
        id_adresse=self.fetchAdresseByData(patientData)
       
        if id_adresse==None :
             self.cursor=self.getCursor()
             sqla = """INSERT INTO adresse(numero, rue, cp, ville) VALUE (%s,%s,%s,%s);"""
             vala =(patientData.get('numero'), patientData.get('rue'), patientData.get('cp'), patientData.get('ville'))
             self.cursor.execute(sqla, vala)
             id_adresse=self.fetchAdresseByData(patientData)
             
                 
        self.cursor=self.getCursor()
        sql = """INSERT INTO patient (adresse_idadresse, infirmier_idinfirmier, 
              nom, prenom, naissance, sexe, securite_sociale)
              VALUES (%s, %s, %s, %s, %s, %s, %s);"""
        val = (id_adresse,id_infirmier, patientData.get('nom'),  patientData.get('prenom'), patientData.get('naissance'),  patientData.get('sexe'),   patientData.get('securite_sociale') )
            
        self.cursor.execute(sql, val)
        self.cursor.close()

     

    def update(self, patientData, idpatient, idadresse):
        """[cette methode sert à mettre à jour les informations dun patient dans la table patient 
        et son adresse dans la table adresse]

        Args:
                patientData ([dict]): [les infos du patients]
                idpatient : identifiant patient à mettre à jour
                idadresse : id adresse correspondant à patient
        """
        try :
            if type(patientData.get('numero_pro')).__name__ != 'NoneType':
                id_infirmier = self.fetchOneInfirmier(patientData)
            #id_adresse=self.fetchAdresseByData(patientData)
            # if id_adresse==None :
            #     self.cursor=self.getCursor()
            #     sqla = """INSERT INTO adresse(numero, rue, cp, ville) VALUE (%s,%s,%s,%s);"""
            #     vala =(patientData.get('numero'), patientData.get('rue'), patientData.get('cp'), patientData.get('ville'))
            #     self.cursor.execute(sqla, vala)
            #     id_adresse=self.fetchAdresseByData(patientData)
            
            self.cursor = self.getCursor()
            sqlp = f"""UPDATE patient SET nom='{patientData.get('nom')}', 
                prenom='{patientData.get('prenom')}',naissance='{patientData.get('naissance')}',
               sexe='{patientData.get('sexe')}', infirmier_idinfirmier='{id_infirmier}', adresse_idadresse='{idadresse}' where idpatient like '{idpatient}'"""

            sqla = f"""UPDATE adresse SET numero='{patientData.get('numero')}',
                  rue='{patientData.get('rue')}', ville='{patientData.get('ville')}', 
                 cp='{patientData.get('cp')}'where idadresse like '{idadresse}'"""

            self.cursor.execute(sqlp)
            self.cursor.execute(sqla)
            self.cursor.close()
        except :
            print("Veuillez s'assurer que toute les informations sont remplies")
     
            
    
    def delete(self, id):
        self.cursor=self.getCursor()
        sql = f"DELETE FROM patient WHERE idpatient = {id}"
        self.cursor.execute(sql)
        self.cursor.close()
    def fetchInfirmier(self):
        """[Methode qui permet de récuper nom, prénom, numéro_pro infirmier]

        Returns:
            [dict]: [nom, prenom, numero_pro]
        """
        self.cursor=self.getCursor()
        sqlp="SELECT nom, prenom, numero_pro FROM infirmier"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchall()
        self.cursor.close()
        return rows 
    
    #---------------------------------Useful method----------------------------------------------------------------------#
    def fetchInfirmierByIdPatient(self, patientData):
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
    
    def fetchAdresseByData(self, patientData):
        # recuperer l'id de l'adresse si elle existe
        try :
           self.cursor=self.getCursor()
           sqlSelect=f"SELECT idadresse FROM adresse WHERE adresse.numero='{patientData.get('numero')}' and  adresse.rue= '{patientData.get('rue')}' and adresse.cp='{patientData.get('cp')}' and adresse.ville='{patientData.get('ville')}';"
         
           self.cursor.execute(sqlSelect)
          
           rows=self.cursor.fetchone()
           print("JE Samy", rows)
           self.cursor.close()
           
           if rows!=None:
             
               return rows.get("idadresse")
        except InternalError as er:
            print(er)
            
              
    

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
        if rows!=None:
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
    

    