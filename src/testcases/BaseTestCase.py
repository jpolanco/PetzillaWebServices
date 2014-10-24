from unittest import TestCase

__author__ = 'polanco'


from src.framework.utilities import JsonLists, MongoDBManager
from src.framework.utilities.ConstantClass import *
from src.framework.setup.ServerConnection import Server_Connection_v2,SeverConnection


class BaseTestCase(TestCase):

    def __init__(self, methodName='runTest'):
        super(BaseTestCase, self).__init__(methodName)
        self.utilities = Utilities()
        self.constant_class = ConstantClass()
        self.server_connection = SeverConnection()
        self.server_connection_v2 = Server_Connection_v2()
        self.json_lists = JsonLists.JsonLists()
        self.resource_test_cases = Test_Cases_Resources()
        self.mongo_db_manager = MongoDBManager.DBConnector()