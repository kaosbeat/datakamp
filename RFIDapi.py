import requests
import json


def logAction(readerid, visitorid, actionid):
# POST /api/log
# Content-Type: application/json
# Body:
# {
#   "reader-id": "00:11:22:33:44:55",
#   "visitor-id": "de:ca:fb:ad:27:08",
#   "action-id": 10
# } 
	
	data = {"reader-id": str(readerid), "visitor-id": str(visitorid), "action-id": str(actionid)}
	# params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}
	# data = 
	# data = { "reader-id": "00:11:22:33:44:55", "visitor-id": "de:ca:fb:ad:27:08", "action-id": "A00"}
	print data
	

	endpoint = "http://35.157.49.30:8080/api/log"
	print("now posting")
	response = requests.post(endpoint, json=data)
	if (response.status_code == 201):
		print("succesfully logged action")
		print("status_code" + str(response.status_code))
	else:
		print("something went wrong")
		print("status_code" + str(response.status_code))
		return False
	# return response.content
