from model.db import Db

class Infirmier(Db):
    def __init__(self):
        super().__init__()
    
    def fetchAll(self):
        self.cursor=self.getCursor()
        sqlp=f"SELECT nom, prenom, numero_pro, idinfirmier FROM infirmier"
        self.cursor.execute(sqlp)
        rows=self.cursor.fetchall()
        self.cursor.close()
        return rows
    
    def deleteById(self, id):
        self.cursor=self.getCursor()
        sql = f"DELETE FROM infirmier WHERE idinfirmier = {id}"
        self.cursor.execute(sql)
        self.cursor.close()
        
        
        
    def fetchAdresse(self, infirmierData):
        """[Methode qui permet de récuper l'idadresse à partir du numéro/rue ville et cp]

        Args:
            infirmierData ([type]): [description]

        Returns:
            [int]: [le idadresse]
        """
        self.cursor=self.getCursor()
        sqlSelect=f"""SELECT idadresse FROM adresse WHERE adresse.numero='{infirmierData.get('numero')}'
        and  adresse.rue= '{infirmierData.get('rue')}'and adresse.cp='{infirmierData.get('cp')}' 
        and adresse.ville='{infirmierData.get('ville')}';"""
        self.cursor.execute(sqlSelect)
        rows=self.cursor.fetchone()
        self.cursor.close()
        if (type(rows).__name__!= "NoneType") :
            return rows.get('idadresse')
    

    def addInfirmier(self, infirmierData):
        """[cette methode sert à ajouter un infirmier dans la base medical, table infirmier]

        Args:
            infirmierData ([dict]): [les infos de l'infirmier]
        """
        id_adresse=None
        
        # if type(infirmierData.get('numero')).__name__!= "NoneType" :
        id_adresse=self.fetchAdresse(infirmierData)
        if id_adresse==None :
            self.cursor=self.getCursor()
            sqla = """INSERT INTO adresse(numero, rue, cp, ville) VALUE (%s,%s,%s,%s);"""
            vala =(infirmierData.get('numero'), infirmierData.get('rue'), infirmierData.get('cp'), infirmierData.get('ville'))
            self.cursor.execute(sqla, vala)
            id_adresse==self.fetchAdresse(infirmierData)
        
        self.cursor=self.getCursor()
        sqlb = """INSERT INTO infirmier (adresse_idadresse, numero_pro, nom, prenom, tel_pro, tel_perso)
                VALUES (%s, %s, %s, %s, %s, %s);"""
        valb = (id_adresse, infirmierData.get('numero_pro'), infirmierData.get('nom'), infirmierData.get('prenom'), infirmierData.get('tel_pro'), infirmierData.get('tel_perso'))
        
        self.cursor.execute(sqlb, valb)
        self.cursor.close()

