from src.framework.utilities import ConstantClass
from src.testcases.BaseTestCase import BaseTestCase

__author__ = 'polanco'


class Login_User_Test_Cases(BaseTestCase):

     def __init__(self, methodName='runTest'):
        super(Login_User_Test_Cases, self).__init__(methodName)
        self.url = "{}{}".format(ConstantClass.ConstantClass.HOST_URL,
                                 ConstantClass.ConstantClass.REGISTRATION_USER_PATH)