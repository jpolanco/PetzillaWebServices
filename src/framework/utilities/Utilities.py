__author__ = 'polanco'

import urllib
import base64
from random import randint

class Utilities(object):

    def get_json_value(self, json_string, key_value):
        value_return = ''

        if not json_string:
            return value_return
        else:
          self.value_return = json_string[key_value]

        return self.value_return

    def json_constructor(self, json_string):
         return urllib.urlencode(json_string)

    @staticmethod
    def image_base64_encoder(file_path="./resources/images/animal.jpg"):
        with open(file_path, 'r') as imageFile:
            return base64.urlsafe_b64encode(base64.b64decode(imageFile.read()))

    @staticmethod
    def random_number_generator():
        return randint(0, 10000000)

    @staticmethod
    def get_random_email_and_user(name="jpolanco+{}", host="@gmail.com"):
        ran = Utilities.random_number_generator()
        newName = name.format(ran)
        return newName, newName + host
