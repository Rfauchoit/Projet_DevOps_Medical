from model.db import Db

class Infirmier(Db):
    def __init__(self):
        super().__init__()
    
    def fetchAll(self):
        self.cursor=self.getCursor()
        sqlp=f"SELECT nom, prenom, numero_pro, idinfirmier, tel_pro, tel_perso, adresse_idadresse FROM infirmier"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchall()
        self.cursor.close()
        return rows
    
    def fetchAdresseByID(self, idadresse):
        self.cursor=self.getCursor()
        sqlp=f"SELECT rue, numero, ville, cp, idadresse FROM adresse where idadresse='{idadresse}'"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchone()
        self.cursor.close()
        return rows 
    
    def fetchAdresseByData(self, InfirmierData):
        # recuperer l'id de l'adresse si elle existe
        self.cursor=self.getCursor()
        sqlSelect=f"SELECT idadresse FROM adresse WHERE adresse.numero='{InfirmierData.get('numero')}' and  adresse.rue= '{InfirmierData.get('rue')}' and adresse.cp='{InfirmierData.get('cp')}' and adresse.ville='{InfirmierData.get('ville')}' ;"
        self.cursor.execute(sqlSelect)
        rows=self.cursor.fetchone()
    
        if (type(rows).__name__!= "NoneType") :
            return rows.get('idadresse')
    
    def deleteById(self, id):
        self.cursor=self.getCursor()
        sql = f"DELETE FROM infirmier WHERE idinfirmier = {id}"
        self.cursor.execute(sql)
        self.cursor.close()
        
    def updateinfirmier(self, infirmierData):
    
        """[cette methode sert à mettre à jour les informations dun infirmier dans la table infirmier 
        et son adresse dans la table adresse]

        Args:
                
        """
        
        idadresse=self.fetchAdresseByData(infirmierData)
        if idadresse==None :
             self.cursor=self.getCursor()
             sqla = """INSERT INTO adresse(numero, rue, cp, ville) VALUE (%s,%s,%s,%s);"""
             vala =(infirmierData.get('numero'), infirmierData.get('rue'), infirmierData.get('cp'), infirmierData.get('ville'))
             self.cursor.execute(sqla, vala)
             idadresse=self.fetchAdresseByData(infirmierData)
            
        print("Infirmier ",idadresse )
        self.cursor = self.getCursor()
        sqlp = f"""UPDATE infirmier SET nom='{infirmierData.get('nom')}', 
                prenom='{infirmierData.get('prenom')}',tel_pro='{infirmierData.get('tel_pro')}',
                tel_perso='{infirmierData.get('tel_perso')}', adresse_idadresse='{idadresse}' where numero_pro like '{infirmierData.get('numero_pro')}'"""

        sqla = f"""UPDATE adresse SET numero='{infirmierData.get('numero')}',
                  rue='{infirmierData.get('rue')}', ville='{infirmierData.get('ville')}', 
                 cp='{infirmierData.get('cp')}'where idadresse like '{idadresse}'"""

        self.cursor.execute(sqlp)
        self.cursor.execute(sqla)
        self.cursor.close()
