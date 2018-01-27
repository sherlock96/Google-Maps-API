# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 03:49:49 2018

@author: shiva
"""

import urllib
import json

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCLNO5mol_LjqDuOkTKLBke4Q9de-6GVy4'

origin = raw_input('Where are you?: ').replace(' ','+')
destination = raw_input('Where do you want to go?: ').replace(' ','+')

nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request

response = urllib.urlopen(request).read()

directions=json.loads(response)
#directions = json.dumps(json.loads(response))
#print(directions)

directions.keys()

routes=directions["routes"]
legs=routes[0]["legs"]
print("Leg distance is- ")
print(legs[0]["distance"]["text"])
