#Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector

class User():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                password='pass',
                                host='localhost',
                                port=3306,
                                database='movies')
        self.cursor = self.conn.cursor()