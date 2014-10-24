__author__ = 'polanco'

from src.framework.utilities.Utilities import Utilities

class ConstantClass(object):

    HTTP_HEADER = {"version": "2", "Content-Type": "application/json"}
    HOST_URL = 'https://qa4.petzila.com/'
    POST_REQUEST = 'POST'
    GET_REQUEST = 'GET'
    DELETE_REQUEST = 'DELETE'

    #----------MONGO DATABASE CONSTANTS--------#
    DB_HOST = "50.17.144.210"
    DB_PORT = 27017
    DB_NAME = "petzidb"
    DB_USER_COLLECTION = "User"

    #----------API PATHS--------#
    REGISTRATION_USER_PATH = 'api/user/signup'
    ACTIVATION_ACCOUNT_PATH = 'api/user/accountActivation'

    #----------GLOBAL_USER-------#
    GLOBAL_USER = None




class Test_Cases_Resources(object):

    @staticmethod
    def get_registration_user_values():
        username, email = Utilities.get_random_email_and_user()
        registration_user_values = {"email": email,
                                    "password": "12345678",
                                    "username": username,
                                    "profilePicture": Utilities.image_base64_encoder(),
                                    "resourceType": "image/jpeg",
                                    "description": "",
                                    "firstName": "Juan",
                                    "lastName": "Polanco",
                                    "country": "",
                                    "city": "",
                                    "zipCode": "",
                                    "signupType": "local",
                                    "socialNetworkID": ""
                                    }
        return registration_user_values