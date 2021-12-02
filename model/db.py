from flask import config
import mysql.connector
from abc import ABC
from model.config import Config

class Db():
    
    def __init__(self):
        self.logging()

    def logging(self):
        self.conn = mysql.connector.connect(
            user=Config.user,
            password=Config.password,
            host=Config.host,
            database=Config.database,
            port=Config.port,
            )
            
        self.conn.autocommit=True #il est à zero par defaut sur mysql.connector
       

    def getCursor(self):
        try:
           cursor = self.conn.cursor(dictionary=True)
          
           return cursor
        except mysql.connector.Error as err:
           print(err)

        self.conn.autocommit=True 


    def getCursor(self):
        try:
            cursor = self.conn.cursor(dictionary=True)
            return cursor
        except mysql.connector.Error as err:
            print(err)
            


