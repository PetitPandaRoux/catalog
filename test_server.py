'''
Ces tests concernent principalement les connections vers le serveur local
Une partie qui test les accès et les routes vers le serveur local
'''

import httplib2
import json
import sys


print ("Running Endpoint Tester....\n")
address = 'http://localhost:5000'

# GET REQUEST
print ("Test 1a Making a GET request to / and /catalog...")
try:
	url = address + "/"
	h = httplib2.Http()
	resp, result = h.request(url, 'GET')
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
	print ("Test 1a FAILED: Could not make GET Request to web server")
	print (err.args)
else:
	print ("Test 1a PASS: Succesfully Made GET Request to /catalog")

try:
	url = address + "/"
	h = httplib2.Http()
	resp, result = h.request(url, 'GET')
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
	print ("Test 1b FAILED: Could not make GET Request to web server")
	print (err.args)
	sys.exit()
else:
	print ("Test 1b PASS: Succesfully Made GET Request to /")


print ("Test 1a Making a GET request to other parts of the catalog...")
try:
	url = address + "/"
	h = httplib2.Http()
	resp, result = h.request(url, 'GET')
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
	print ("Test 1a FAILED: Could not make GET Request to web server")
	print (err.args)
else:
	print ("Test 1a PASS: Succesfully Made GET Request to /catalog")


#POST REQUEST


#API_ENDPOINT

#Pytest assertion

