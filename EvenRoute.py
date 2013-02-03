# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=11808
'''

import TopCoder

class EvenRoute(TopCoder.TopCoder):

	possible = 'CAN'
	impossible = 'CANNOT'

	def getPoints(self):
		result = []
		for i in range(len(self.x)): 
			result.append([self.x[i], self.y[i]])
		return result

	def traverse(self, origin, points):
		for offsetX in range(0,1):
			for offsetY in range(0,1):
				for j in range(len(points)):
					if origin[0] + offsetX == points[j][0] and origin[1].offsetY == points[j][1]:
						points.pop(j)

						

	def isItPossible(self):
		pos = [0,0] 
		points = self.getPoints()
		for i in range(len(points)):
		
		

def main():
	evenRoute = EvenRoute()
	evenRoute.setSolverMethod(evenRoute.isItPossible)
	evenRoute.setMode(evenRoute.MODE_DEBUG)
	evenRoute.solve({'x': [-1, -1, 1, 1], 'y': [-1, 1,1,-1], 'wantedParity': 0}, 'CAN')


if __name__ == '__main__':
	main()

