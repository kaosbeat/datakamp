import requests
import json
import random


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
		returndata = { "totalscans": random.randint(1,68), "currentplan": "VIP", "name" : "Pierke", "lastname": "Van Gent" }
		return returndata
	else:
		print("something went wrong")
		print("status_code" + str(response.status_code))
		return False
	# return response.content
