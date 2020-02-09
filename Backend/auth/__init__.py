'''
	OAuth v2 Signin Functionality
'''

import oauthlib
import hashlib
import os

def checkValidAuth(database, userid, giventoken):
	'''
	Check if the authentication token provided by a user is valid.
	Returns true or false.
	Takes the userID, the given token, and the database
	'''
	return False

def genOauthRequest(database, userid):
	'''
	Prepare to validate using oauth and generate a link
	returns a string containing the valid request
	'''
	forgeryPrevention = hashlib.sha256(os.urandom(1024)).hexdigest() #Generate a long token to prevent auth forgery


def createNewUser(database):
	'''
	Create a database entry for a new user. This will be called if a user creates an account for the first time.
	'''
	possibleID = random.randint(0, 4294967295) #Generate a new ID between 0 and the 32 bit integer limit

	if database["users"].find_one({"userid":str(possibleID)}) == None: #Check if the ID already exists
		

	else:
		#In the absolutely amazingly unlikely event that the generated ID already exists, generate a new one
		return createNewUser(database)