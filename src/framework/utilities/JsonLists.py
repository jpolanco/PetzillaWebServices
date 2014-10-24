__author__ = 'polanco'

import json
import logging

class JsonLists(object):

    def registration_user_JSON(self, username, email, password, profilePicture, resourceType, description, firstName,
                               lastName, country, city, zipCode, signupType, socialNetworkID):
        json_data = None
        try:
            json_data = open("./resources/jsonfiles/registration.json", 'r')
            data = json.load(json_data)
            data['email'] = email
            data['password'] = password
            data['username'] = username
            data['profilePicture'] = profilePicture
            data['resourceType'] = resourceType
            data['description'] = description
            data['name']['firstName'] = firstName
            data['name']['lastName'] = lastName
            data['location']['country'] = country
            data['location']['city'] = city
            data['location']['zipCode'] = zipCode
            data['signupType'] = signupType
            data['socialNetworkID'] = socialNetworkID
        finally:
            if json_data:
                json_data.close()
            else:
                logging.critical("Can't load Registration.JSON please check the path")
                raise IOError("Registration File Does not Exist")


        return json.dumps(data)