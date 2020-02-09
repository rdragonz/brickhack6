import math


def calcPoint(direction, distance, lat, lon):
	'''
	Calculates a second point based on an input point, distance, and bearing
	direction designations are detailed below, this can be floats if desired
	Returns a tuple with a new point
	'''

	#0 = North
	#1 = East
	#2 = South
	#3 = West

	R = 6378.1 #Radius of the Earth
	brng = direction * 1.57 #Bearing is 90 degrees converted to radians.
	d = distance * 1.60934 #Distance in miles

	lat1 = lat * (math.pi * 180) #Current lat point converted to radians
	lon1 = lon * (math.pi * 180) #Current long point converted to radians

	lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
	             math.cos(lat1)*math.sin(d/R)*math.cos(brng))

	lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
	                     math.cos(d/R)-math.sin(lat1)*math.sin(lat2))

	return (lat2, lon2)
