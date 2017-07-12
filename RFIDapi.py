import requests
import json
import random

def remapID(ID):
	if (ID == "794676E4"):
		return "12c86ca87939"
	else:
		return "12:c7:54:29:07:1b"

def logAction(readerid, visitorid, actionid):

	data = { "reader-id": readerid, "visitor-id": visitorid, "action-id": actionid}
	print data

	endpoint = "https://cirqatron.datakamp.be/api/log"
	print("now posting")
	response = requests.post(endpoint, auth=('chips', 'iM8ShaiToon5apha'), json=data)
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
    
def logOnboarding(readerid, visitorid):

	data = { "reader-id": readerid, "visitor-id": visitorid, "action-id": actionid}
	print data

	endpoint = "https://onboarding.datakamp.be/read-id"
	print("now posting")
	response = requests.post(endpoint, auth=('cirq', 'calmD0wn1337!'), json=data)
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

#def logIngang(readerid, visitorid, actionid):
#
#	data = { "reader-id": readerid, "visitor-id": visitorid, "action-id": "A00"}
#	print data
#	endpoint = "http://35.157.49.30:8080/api/log"
#	print("now posting Ingang")
#	response = requests.post(endpoint, json=data)
#	if (response.status_code == 201):
#		print("succesfully logged action")
#		print("status_code" + str(response.status_code))
#		# return (random.randint(3))
#		# returndata = { "totalscans": random.randint(1,68), "currentplan": "VIP", "name" : "Pierke", "lastname": "Van Gent" }
#		return response.status_code
#	else:
#		print("something went wrong")
#		print("status_code" + str(response.status_code))
#		return False
#	# return response.content

def getVistorActions(visitorid):
	#visitorid = remapID(visitorid)
	endpoint = "https://cirqatron.datakamp.be/api/checkvisitor/" + str(visitorid)
	endpoint ="http://35.157.49.30:8080/api/checkvisitor/12c86ca87939"
	print("now getting " + endpoint)
	response = requests.get(endpoint, auth=('chips', 'iM8ShaiToon5apha'))
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
#def logKassa(readerid, visitorid, actionid):
	data = { "reader-id": readerid, "visitor-id": visitorid, "action-id": "ADK"}
	print data
	endpoint = "https://cirqatron.datakamp.be/api/log"
#	print("now posting")
	response = requests.post(endpoint, auth=('chips', 'iM8ShaiToon5apha'), json=data)
	if (response.status_code == 201):
#		print("succesfully logged action")
#		print("status_code" + str(response.status_code))
		# return (random.randint(3))
		# returndata = { "totalscans": random.randint(1,68), "currentplan": "VIP", "name" : "Pierke", "lastname": "Van Gent" }
		return response.status_code
	else:
		print("something went wrong")
		print("status_code" + str(response.status_code))
		return False
	# return response.content
def logBar(readerid, visitorid, actionid):
	endpoint = "https://cirqatron.datakamp.be/api/checkvisitor/" + str(visitorid)
	print("now getting" + endpoint)
	response = requests.get(endpoint, auth=('chips', 'iM8ShaiToon5apha'))
	if (response.status_code == 200):
		print("succesfully logged action")
		print("status_code" + str(response.status_code))
		# return (random.randint(3))
		# returndata = { "totalscans": random.randint(1,68), "currentplan": "VIP", "name" : "Pierke", "lastname": "Van Gent" }
        	returndata = response.json()
        	return returndata
	else:
		print("something went wrong")
		print("status_code" + str(response.status_code))
		return False
	# return response.content
#def logStem(readerid, visitorid, actionid):
	data = { "reader-id": readerid, "visitor-id": visitorid, "action-id": "AA"}
	print data
	endpoint = "https://cirqatron.datakamp.be/api/log"
	print("now posting")
	response = requests.post(endpoint, auth=('chips', 'iM8ShaiToon5apha'), json=data)
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
    #Playfield-kot ==> unieke action id??
#def logPlay(readerid, visitorid, actionid):
	data = { "reader-id": readerid, "visitor-id": visitorid, "action-id": "play"}
	print data
	endpoint = "https://cirqatron.datakamp.be/api/log"
	print("now posting")
	response = requests.post(endpoint, auth=('chips', 'iM8ShaiToon5apha'), json=data)
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
