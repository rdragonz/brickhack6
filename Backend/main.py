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
from config import * #Import all variables from the config file

app = flask.Flask(__name__) #Create the flask instance


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
	'''
	app.run(debug=True, host='0.0.0.0') 

if __name__ == '__main__':
	main()