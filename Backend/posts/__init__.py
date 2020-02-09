import random
import datetime

def newPostID(database):
	'''
	Generate a new post ID.
	Needs a database object to verify that the ID doesn't already exist
	'''
	possibleID = random.randint(0, 4294967295) #Generate a new ID between 0 and the 32 bit integer limit

	if database["posts"].find_one({"postid":possibleID}) == None: #Check if the ID already exists
		return possibleID
	else:
		#In the absolutely amazingly unlikely event that the generated ID already exists, generate a new one
		return newPostID(database)

def newTextPost(database, userid, lat, lon, text, tags):
	'''
	Create a new post with text
	'''
	postID = newPostID(database) #Create a new valid ID

	time = datetime.datetime.now(datetime.timezone.utc) #Get the current UTC time

	database['posts'].insert_one({"postid" : postID,"userid" : userid, "type" : "text", "timestamp" : str(time), "lat": lat, "lon": lon, "content" : { "text" : text },
    "tags" : tags})