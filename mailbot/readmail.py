# Importing required libraries
from googleapiclient import discovery
from googleapiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
import base64
import re
import time
import dateutil.parser as parser
from datetime import datetime
import datetime
import csv
import re	
import requests
import time
from sendmail import create_message 

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os
# Creating a storage.JSON file with authentication details
SCOPES = 'https://www.googleapis.com/auth/gmail.modify' # we are using modify and not readonly, as we will be marking the messages Read
store = file.Storage('storage.json') 
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

user_id =  'me'
label_id_one = 'INBOX'
label_id_two = 'UNREAD'
	
# Getting all the unread messages from Inbox
# labelIds can be changed accordingly

while(True):
	unread_msgs = GMAIL.users().messages().list(userId='me',labelIds=[label_id_one, label_id_two]).execute()
	print(unread_msgs)
	if not unread_msgs or 'messages' not in unread_msgs:
		time.sleep(5)
		continue
	# We get a dictonary. Now reading values for the key 'messages'
	mssg_list = unread_msgs['messages']
	if not mssg_list:
		time.sleep(5)
		continue

	#print ("Total unread messages in inbox: ", str(len(mssg_list)))

	final_list = [ ]


	for mssg in mssg_list:
		temp_dict = { }
		m_id = mssg['id'] # get id of individual message
		message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute() # fetch the message using API
		payld = message['payload'] # get payload of the message 
		headr = payld['headers'] # get header of the payload
	

		    # Fetching message body
		mssg_parts = payld['parts'] # fetching the message parts
		part_one = mssg_parts[0] # fetching first element of the part
		part_body = part_one['body'] # fetching body of the message
		part_data = part_body['data'] # fetching data from the body
		clean_one = part_data.replace("-","+") # decoding from Base64 to UTF-8
		clean_one = clean_one.replace("_","/") # decoding from Base64 to UTF-8
		clean_two = base64.b64decode (bytes(clean_one, "UTF-8")) # decoding from Base64 to UTF-8
		
		clean_two = clean_two.decode("utf-8")
		
		office = "San Francisco"
		
		line_count = 0
		for line in clean_two.split('\r\n'):
			if "Subject: Arrived:" in line:
				restaurant = " ".join(line.split()[2:])
			if "To: " in line:
				email = line.split()[1]

			if "Date/Time" in line: 
				break
			line_count += 1

		food = ""
		for line in clean_two.split('\r\n')[(line_count+3):]:
			if "Notes:" in line:
				continue
			if "Update" in line:
				break
			if "For: " not in line: 
				food = food + line + '\n'
			else: 
				name = " ".join(line.split()[1:-1])
			
		
		GMAIL.users().messages().modify(userId=user_id, id=m_id,body={ 'removeLabelIds': ['UNREAD']}).execute() 
		
<<<<<<< HEAD
		r = requests.post("http://localhost:8000/create", data={'office': office, 'name': name, 'description': food, 'restaurant': restaurant, 'email': email})
		message_text = "Your food was claimed, thank you!"
		subject = "Claimed!"
=======
		r = requests.post("http://localhost:8000/create", json={'office': office, 'name': name, 'description': food, 'restaurant': restaurant, 'email': email})
>>>>>>> c2c8f3bfed1918ced6cc66c495dc972d63e64655
	time.sleep(5)
			
		
