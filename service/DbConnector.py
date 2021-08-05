import os
import pymongo

'''
 Mongo DB connector 
 provide connection instance
'''
class DbConnector:

    def __init__(self):
        self.__connection = None

    def connect(self):
        """
        Used Singleton pattern so in every call,
        without create new instance, same connection will be returned
        :return: connection instance
        """
        if not self.__connection:
            self.__connection = pymongo.MongoClient(
                "mongodb+srv://" + os.getenv("DB_USERNAME") + ":" + os.getenv("DB_PASSWORD") + "@" + os.getenv(
                    'DB_HOST') + "/" + os.getenv('DB_COLLECTION'))
        return self.__connection

    def __call__(self):
        """
        prevent direct object call
        """
        raise TypeError('DbConnector must be accessed through `connect()`.')
