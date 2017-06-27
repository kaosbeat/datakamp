import requests
import json
import random

def remapID(ID):
	if (ID == "794676E4"):
		return "12c86ca87939"
	else:
		return "12:c7:54:29:07:1b"

def logAction(readerid, visitorid, actionid):

	data = { "reader-id": readerid, "visitor-id": visitorid, "action-id": "A00"}
	print data
	endpoint = "http://35.157.49.30:8080/api/log"
	print("now posting")
	response = requests.post(endpoint, json=data)
	if (response.status_code == 201):
		print("succesfully logged action")
		print("status_code" + str(response.status_code))
		# return (random.randint(3))
		# returndata = { "totalscans": random.randint(1,68), "currentplan": "VIP", "name" : "Pierke", "lastname": "Van Gent" }
		return response.status_code
	else:
		print("something went wrong")
		print("status_code" + str(response.status_code))
		return False
	# return response.content



def getVistorActions(visitorid):
	visitorid = remapID(visitorid)
	endpoint = "http://35.157.49.30:8080/api/checkvisitor/" + str(visitorid)
	# endpoint ="http://35.157.49.30:8080/api/checkvisitor/12c86ca87939"
	print("now getting " + endpoint)
	response = requests.get(endpoint)
	if (response.status_code == 200):
		print("succesfully got data")
		print("status_code= " + str(response.status_code))
		# return (random.randint(3))
		returndata = response.json()
		return returndata
	else:
		print("something went wrong while getting visitordata")
		print("status_code" + str(response.status_code))
		return False
	# return response.content