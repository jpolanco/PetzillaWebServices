import json
from src.framework.utilities import ConstantClass
import requests

__author__ = 'polanco'

import urllib2


class SeverConnection(object):
    def __init__(self):
        self.response_json = None
        self.response_code = None

    def connect_to_server(self, url, json_body=None):
        request = urllib2.Request(url, json_body, ConstantClass.ConstantClass.HTTP_HEADER)
        try:
            response = urllib2.urlopen(request)
            self.response_code = response.code
            self.response_json = json.loads(response.read())
        except urllib2.HTTPError as error:
            self.response_code = error.code
            self.response_json = error.msg

    def get_response_json(self):
        return self.response_json

    def get_response_code(self):
        return self.response_code


class Server_Connection_v2(object):

    def __init__(self):
        self.response_code = None
        self.response__body = None

    def connect_to_server(self, url, request_type, param=None):
        response = None

        if request_type is ConstantClass.ConstantClass.GET_REQUEST:
            response = requests.get(url, params=param, headers=ConstantClass.ConstantClass.HTTP_HEADER)

        elif request_type is ConstantClass.ConstantClass.POST_REQUEST:
            response = requests.post(url, data=param, headers=ConstantClass.ConstantClass.HTTP_HEADER)

        self.response_code = response.status_code
        self.response_body = json.loads(response.content)


    def get_response_body(self):
        return self.response_body

    def get_response_code(self):
        return self.response_code