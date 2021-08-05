import os
from service.DbConnector import DbConnector

'''
 Default model for create the connection and contain it 
 for further use. also get the database name in db properties
'''
class Model:
    def __init__(self):
        self.connection = DbConnector().connect()
        self.db = self.connection[os.getenv("DB_COLLECTION", 'optimaanalytics')]

