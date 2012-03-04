# -*- coding: utf-8 -*-
'''
Problem Statement
    
A traveling salesman has recently decided to go international and sell his wares around the globe. 
He has done in depth research and has come up with a list of cities which he thinks will provide the best market for his goods. 
In planning his trip, the salesman wants to minimize the total distance he has to travel because he does not particularly like 
traveling (which is unfortunate for him, as he is a traveling salesman) and furthermore, he figures the less distance he has to travel, 
the cheaper his trip will be. 

However, this salesman is not particularily good at math, and so you must write a computer program to help him find his way in the least distance.
You will be given a set of cities defined by their longitudes and latitudes. 
In addition, you will be given the radius of the planet that this traveling salesman resides on. 
Assume that there are direct flights, both ways, between every pair of cities that the salesman wants to visit, and that the flights 
follow the shortest path possible (over the surface of the planet). In addition, the first element of the input String[] 
will be the city in which the salesman lives, and thus his trip must start and end at this city.

Each city is defined by two numbers, a latitude and a longitude. 

The latitude is the number of degrees above the equator, with 90 being the north pole, and -90 being the south pole. 
The longitude is the number of degrees east or west of some arbitrary, predefined point. 

Thus, 90 degrees east is one quarter of the way around the globe in the eastern direction.
If the result is not an integer, round it to the nearest integer (.5 rounds up)

Definition
    
Class:
Travel
Method:
shortest
Parameters:
String[], int
Returns:
int
Method signature:
int shortest(String[] cities, int radius)
(be sure your method is public)
    

Notes
-
Assume the planet is a perfect sphere.
-
To find the cartesion coordinates of a city, assuming the center of the planet is at (0,0,0), use the following formulas: 
	x = r*cos(latitude)*cos(longitude) 
	y = r*cos(latitude)*sin(longitude) 
	z = r*sin(latitude)
	
Constraints
-
cities contains between 2 and 9 elements, inclusive.
-
Each element of cities represents a unique point on the globe.
-
Each element of cities is formatted as "<latitude> <longitude>" where <latitude> is an integer in the range -90 to 90, inclusive, and <longitude> is an integer in the range -180 to 180, inclusive.
-
radius is an integer between 1 and 1,000, inclusive.
-
to avoid rounding errors, the shortest path, prior to rounding, will not be within 0.001 of <x>+0.5 for any integer <x>.
Examples
0)

    
{"0 0","0 1"}
1000
Returns: 35
The two cities are located one degree apart at the same latitude
1)

    
{"0 0","0 1","0 -1","-1 0","1 0","-1 -1","1 1","1 -1","-1 1"}
1
Returns: 0

2)

    
{"40 -82","-27 -59","-40 48"
,"26 -12","-31 -37","-30 42"
,"-36 -23","-26 71","-19 83","8 63"}
698
Returns: 4505

'''
import math

'''
x = r*cos(latitude)*cos(longitude) y = r*cos(latitude)*sin(longitude) z = r*sin(latitude)
'''
class Position():
	x = 0
	y = 0
	z = 0
	latitude = 0
	longitude = 0
	radius = 0
	def __init__(self, coord, radius):
		coord = coord.split(' ')
		self.latitude = math.radians(float(coord[0]))
		self.longitude = math.radians(float(coord[1]))
		self.radius = radius

		self.x = self.radius*math.cos(self.latitude)*math.cos(self.latitude)
		self.y = self.radius*math.cos(self.latitude)*math.sin(self.longitude)
		self.z = self.radius*math.sin(self.latitude)

class Travel():

	def getDistance(self, posA, posB):
		return math.sqrt((posB.x-posA.x)**2+(posB.y-posA.y)**2+(posB.z-posB.z)**2)	
		
	def shortest(self, cities, radius):
		H = []
		for i in range(len(cities)):
			H.append([])
			for j in range(len(cities)):
				currentOrigin = Position(cities[i], radius)
				currentEnd = Position(cities[j], radius)
				distance = self.getDistance(currentOrigin, currentEnd)
				if i == 0:
					H[i].append(distance)
				elif j < i:
					H[i].append(H[i-1][j])
				else:
					distance+=H[i-1][j]
					H[i].append(distance)
		return int(math.ceil(H[len(cities)-1][len(cities)-1]+self.getDistance(Position(cities[0], radius), Position(cities[len(cities)-1], radius))))

def main():
	travel = Travel()
	print travel.shortest(["0 0","0 1"], 1000)
	print travel.shortest(["0 0","0 1","0 -1","-1 0","1 0","-1 -1","1 1","1 -1","-1 1"], 1)
	print travel.shortest(["40 -82","-27 -59","-40 48" ,"26 -12","-31 -37","-30 42" ,"-36 -23","-26 71","-19 83","8 63"], 698)

if __name__ == '__main__':
	main()
