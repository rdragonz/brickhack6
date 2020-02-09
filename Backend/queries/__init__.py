'''
Code for simple queries
'''


import queries.distance
from bson import json_util


def postsInRadius(database, distance, lat, lon):
	'''
	Query posts based on location
	'''

	#Calculate points
	northPoint = distance.calcPoint(0, distance, lat, lon)
	southPoint = distance.calcPoint(2, distance, lat, lon)
	westPoint = distance.calcPoint(3, distance, lat, lon)
	eastPoint = distance.calcPoint(1, distance, lat, lon)

	#Find the correct query by finding the relationship between the values
	if northPoint > southPoint:
		if eastPoint > westPoint:
			return json.dumps(database['posts'].find([{"$match":{"$and":[{"lat":{"$lt":northPoint}},{"lat":{"$gt":southPoint}},{"lon":{"$lt":westPoint}},{"lon":{"$gt":eastPoint}}]}}]))
		else:
			return json.dumps(database['posts'].find([{"$match":{"$and":[{"lat":{"$lt":northPoint}},{"lat":{"$gt":southPoint}},{"lon":{"$lt":eastPoint}},{"lon":{"$gt":westPoint}}]}}]))
	else:
		if eastPoint > westPoint:
			return json.dumps(database['posts'].find([{"$match":{"$and":[{"lat":{"$lt":southPoint}},{"lat":{"$gt":northPoint}},{"lon":{"$lt":westPoint}},{"lon":{"$gt":eastPoint}}]}}]))
		else:
			return json.dumps(database['posts'].find([{"$match":{"$and":[{"lat":{"$lt":southPoint}},{"lat":{"$gt":northPoint}},{"lon":{"$lt":eastPoint}},{"lon":{"$gt":westPoint}}]}}]))