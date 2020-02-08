'''
	<Name to be determined>
	BrickHack 6
	Made by:
		Red Ziogas
		Kawagga Naggenda
		Michael Sollazzo
		Robin Kim
	in 2020!
	Greetings from Albany and The ROC!
	https://github.com/rdragonz/brickhack6
	This code is licenesed under the GNU General Public License 3.0 (GPLv3). 
	For more information about this license, please visit https://www.gnu.org/licenses/gpl-3.0.en.html 
	or view the LICENSE file included in this repository.
'''

import flask
from flask import render_template
import urllib
import threading
import pymongo
import config #Import all variables from the config file

app = flask.Flask(__name__) #Create the flask instance

@app.route('/')
def index():
	'''
	Show a dummy page for the API if someone goes to the index
	'''
	return render_template('index.html', site=config.WEBSITE_BASEURL) #Return the dummy page

@app.route('/post', methods=['post'])
def post():
	'''
	Create a new post
	Requires the post type
	Post data
	Location
	And Post content at the bare minimum
	Also will require the oauth token for verification
	'''
	return flask.Response(status=204) #Return a no response for now




@app.route('/query', methods=['get'])
def query():
	'''
	Get posts based on a query
	Requires the current user location
	Also requires oauth token
	Additional fields available.
	'''
	return flask.Response(status=204) #Return a no response for now

def main():
	'''
	Main function
	Creates connection, checks database, and then begins serving using flask
	'''
	
	database_socket = "mongodb://{}:{}@{}:{}".format(urllib.parse.quote_plus(config.DB_USER), urllib.parse.quote_plus(config.DB_PASS), urllib.parse.quote_plus(config.DB_ADDRESS), urllib.parse.quote_plus(config.DB_PORT)) #Format the socket connection
	print("Connecting to database {} ...".format(database_socket)) #Print socket
	db_server = pymongo.MongoClient(database_socket) #Connect to socket

	try:
		#Check if the database exists
		db_server.server_info()
	except ConnectionFailure:
		print("Unable to connect to server!\nExiting...")
		exit(1) #Exit with an error
	print("Connected to server!")
	
	#Check if the database exists
	print("Checking database...")
	if config.DB_NAME in db_server.list_database_names(): #Check to see if the database exists
		database = db_server[config.DB_NAME] #Open a connection to the database
		print("Connected to database {}.".format(config.DB_NAME))	
	else:
		print("Unable to open database {}, database does not exist!\nHave you run the first time setup script?".format(config.DB_NAME))
		exit(1) #Exit with error
	
	app.run(host='0.0.0.0') #Run the flask app

if __name__ == '__main__':
	main()