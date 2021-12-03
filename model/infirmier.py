from model.db import Db

class Infirmier(Db):
    def __init__(self):
        super().__init__()
    
    #---------------------------CRUD METHODE--------------------------------------------------------------------#
    def read(self):
        self.cursor=self.getCursor()
        sqlp=f"SELECT nom, prenom, numero_pro, idinfirmier, tel_pro, tel_perso, adresse_idadresse FROM infirmier"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchall()
        self.cursor.close()
        return rows
    
    def addInfirmier(self, infirmierData):
        """[cette methode sert à ajouter un infirmier dans la base medical, table infirmier]

        Args:
            infirmierData ([dict]): [les infos de l'infirmier]
        """
        id_adresse=self.fetchAdresseByData(infirmierData)
     
        if id_adresse==None :
            self.cursor=self.getCursor()
            sqla = """INSERT INTO adresse(numero, rue, cp, ville) VALUE (%s,%s,%s,%s);"""
            vala =(infirmierData.get('numero'), infirmierData.get('rue'), infirmierData.get('cp'), infirmierData.get('ville'))
            self.cursor.execute(sqla, vala)
            id_adresse=self.fetchAdresseByData(infirmierData)
        
      
        self.cursor=self.getCursor()
        sqlb = """INSERT INTO infirmier (adresse_idadresse, numero_pro, nom, prenom, tel_pro, tel_perso)
                VALUES (%s, %s, %s, %s, %s, %s);"""
        valb = (id_adresse, infirmierData.get('numero_pro'), infirmierData.get('nom'), infirmierData.get('prenom'), infirmierData.get('tel_pro'), infirmierData.get('tel_perso'))
        
        self.cursor.execute(sqlb, valb)
        self.cursor.close()


    def delete(self, id):
       
        self.cursor=self.getCursor()
        sql = f"DELETE FROM infirmier WHERE idinfirmier = '{id}'"
        self.cursor.execute(sql)
        self.cursor.close()
        

    def update(self, infirmierData):
    
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
#---------------------------------Useful methodes-------------------------------------------------------------------------------#
    def fetchAdresseByID(self, idadresse):
        """[Select les infos d'une adresse en fonction de l'idadresse]
    
        Args:
            idadresse ([int]): [idadresse]
    
        Returns:
            [dict]: [le numéro de la rue, ville, cp]
        """
        self.cursor=self.getCursor()
        sqlp=f"SELECT rue, numero, ville, cp, idadresse FROM adresse where idadresse='{idadresse}'"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchone()
        self.cursor.close()
        return rows 
    
    def fetchAdresseByData(self, InfirmierData):
        """[Select les infos id adresse en fonction du numero de la rue, ville]
    
        Args:
            idadresse ([int]): [idadresse]
    
        Returns:
            [dict]: [id rue]
        """
        self.cursor=self.getCursor()
        sqlSelect=f"SELECT idadresse FROM adresse WHERE adresse.numero='{InfirmierData.get('numero')}' and  adresse.rue= '{InfirmierData.get('rue')}' and adresse.cp='{InfirmierData.get('cp')}' and adresse.ville='{InfirmierData.get('ville')}';"
        self.cursor.execute(sqlSelect)
        rows=self.cursor.fetchone()
    
        if rows!=None:
           
            return rows.get('idadresse')

        
   