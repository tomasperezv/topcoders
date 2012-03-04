# -*- coding: utf-8 -*-
'''
@ee http://community.topcoder.com/stat?c=problem_statement&pm=996
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
