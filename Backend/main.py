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
import json
from flask.ext.openid import OpenID
from flask import g, session

import config #Import all variables from the config file

import posts
import queries

app = flask.Flask(__name__) #Create the flask instance
oid = OpenID(app, '/idstore', safe_roots=[]) #Create an OpenID authenticator

@app.route('/')
def index():
	'''
	Show a dummy page for the API if someone goes to the index
	'''
	return render_template('index.html', site=config.WEBSITE_BASEURL) #Return the dummy page

@app.route('/post', methods=['POST'])
def post():
	'''
	Create a new post
	Requires the post type
	Post data
	Location
	And Post content at the bare minimum
	Also will require the oauth token for verification
	'''
	requestdata = flask.request.json
	if requestdata['type'] == 'text':
		posts.newTextPost(database, requestdata['userid'], requestdata['lat'], requestdata['lon'], requestdata['text'], requestdata['tags'])
	return flask.Response(status=200) #Return 200 OK

@app.route('/login', methods=['get', 'post'])
@oid.loginhandler
def login():
	if g.user is not None:
		return redirect(oid.get_next_url())
	if request.method == 'POST':
		openid = request.form.get('openid')
		if openid:
			return oid.try_login(openid, ask_for=['email', 'fullname', 'image'])
	return render_template('login.html', next=oid.get_next_url(), error=oid.fetch_error())

@app.route('/query', methods=['get'])
def query():
	'''
	Get posts based on a query
	Requires the current user location
	Also requires oauth token
	Additional fields available.
	'''
	requestdata = flask.request.json
	if requestdata['type'] == 'distance':
		return queries.postsInRadius(datbase, requestdata['distance'], requestdata['lat'], requestdata['lon'])
	else:
		return flask.Response(status=400)

@app.before_request
def lookup_current_user():
	g.user = None
	if 'openid' in session:
		openid = session['openid']
		g.user = database["users"].find_one({"openid":openid})
		
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
		global database
		database = db_server[config.DB_NAME] #Open a connection to the database
		print("Connected to database {}.".format(config.DB_NAME))
		print("Checking database structure...")
		if "posts" in database.list_collection_names():
			print("posts collection exists!")
		else:
			print("There's a problem with the database!\nOne or more collections is missing!\nIs this a valid database for this applciation?")
			exit(1) #Exit with error
		if "users" in database.list_collection_names():
			print("users collection exists!")	
		else:
			print("There's a problem with the database!\nOne or more collections is missing!\nIs this a valid database for this applciation?")
			exit(1) #exit with error
		print("Database structure valid!")
	else:
		print("Unable to open database {}, database does not exist!\nHave you run the first time setup script?".format(config.DB_NAME))
		exit(1) #Exit with error

	app.run(debug=True, host='0.0.0.0') #Run the flask app


if __name__ == '__main__':
	main()