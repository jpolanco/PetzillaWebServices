__author__ = 'polanco'

from pymongo import MongoClient
import pymongo
from src.framework.utilities.ConstantClass import ConstantClass


class DBConnector(object):

    def __init__(self):
        self.mongo_connection = None

    def connector(self, host=ConstantClass.DB_HOST, port=ConstantClass.DB_PORT):
        try:
            self.mongo_connection = MongoClient(host, port)
        except pymongo.errors.ConnectionFailure:
            return False

    def find(self, query, collection, db=ConstantClass.DB_NAME):
        self.connector()
        document = self.mongo_connection[db][collection].find_one(query)
        self.mongo_connection.close()
        return document












