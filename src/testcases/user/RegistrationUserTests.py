import json
import base64

__author__ = 'polanco'

import unittest2 as unittest
from proboscis.asserts import assert_true
from proboscis import test
from src.testcases.BaseTestCase import BaseTestCase



from src.framework.utilities import ConstantClass


@test(groups=["webservices", "registrationUser"])
class RegistrationUserTests(BaseTestCase):

    def __init__(self, methodName='runTest'):
        super(RegistrationUserTests, self).__init__(methodName)
        self.url = "{}{}".format(ConstantClass.ConstantClass.HOST_URL,
                                 ConstantClass.ConstantClass.REGISTRATION_USER_PATH)

    def test_registration_user(self):


        #Registration Test
        registration_info = ConstantClass.Test_Cases_Resources.get_registration_user_values()
        self.json_data = self.json_lists.registration_user_JSON(**registration_info)
        assert_true(self.json_data is not None)
        self.server_connection_v2.connect_to_server(self.url,self.constant_class.POST_REQUEST, param=self.json_data)
        #self.server_connection.connect_to_server(self.url, self.json_data)
        assert_true(self.server_connection_v2.get_response_code() == 200,
                    'The response code is not 200 the code displayed is [{0}]'.format(
                        self.server_connection_v2.get_response_code()))
        assert_true(self.server_connection_v2.get_response_body()['status'] == 'Success',
                    "The status is not success is {}".format(self.server_connection.get_response_json()['status']))

        #Activation Test
        """
        username = registration_info['username']
        mongo_document = self.mongo_db_manager.find({'username': username}, 'User')
        activation_key = self.utilities.get_json_value(mongo_document, 'activationKey')
        self.url = "{}{}?key={}".format(self.constant_class.HOST_URL, self.constant_class.ACTIVATION_ACCOUNT_PATH,
                                 activation_key)

        self.server_connection.connect_to_server(self.url)

        assert_true(self.server_connection.get_response_code() == 200,
                    'The response code is not 200 the code displayed is [{0}]'.format(
                        self.server_connection.get_response_code()))

                        """










