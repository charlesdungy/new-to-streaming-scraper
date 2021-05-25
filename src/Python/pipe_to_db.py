from config.config import config
from getpass import getpass
from mysql.connector import connect, Error

class PipeToDB:
    def __init__(self):
        try:
            self.connection = connect(**config)
        except Error as e:
            print(e)

x = PipeToDB()
print(x.connection)