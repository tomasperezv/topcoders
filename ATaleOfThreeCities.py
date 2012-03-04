# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=3543
'''
import math
import TopCoder

class ATaleOfThreeCities(TopCoder.TopCoder):

	def isFirstCity(self, i):
		return i < len(self.a)

	def isSecondCity(self, i):
		return i >= len(self.a) and not self.isThirdCity(i) 

	def isThirdCity(self, i):
		return i >= len(self.a)+len(self.b)

	def hasAllCities(self, i, j, k, l, debug = False):

		hasFirstCity = self.isFirstCity(i) or self.isFirstCity(j) or self.isFirstCity(k) or self.isFirstCity(l)
		hasSecondCity = self.isSecondCity(i) or self.isSecondCity(j) or self.isSecondCity(k) or self.isSecondCity(l)
		hasThirdCity = self.isThirdCity(i) or self.isThirdCity(j) or self.isThirdCity(k) or self.isThirdCity(l)
	
		return hasFirstCity and hasSecondCity and hasThirdCity

	def differentCities(self, i, j):
		return (self.isFirstCity(i) and self.isSecondCity(j)) or (self.isFirstCity(i) and self.isThirdCity(j)) or (self.isSecondCity(i) and self.isThirdCity(j))

	def validPoints(self, totalPoints, i, j, k, l):
		isValid = False

		if i<>j and i<>k and i<>l and j<>k and j<>l and k<>l:
			isValid = True 

		isValid = (isValid and self.hasAllCities(i, j, k, l) and self.differentCities(i,j) and self.differentCities(k,l))

		return isValid

	def getDistance(self, totalPoints, i, j):
		a = totalPoints[i]
		b = totalPoints[j]
		return round(math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2), 4)

	def connect(self):

		totalPoints = self.a + self.b + self.c
		currentDistance = 999999999
		self.log(totalPoints)

		for i in range(len(totalPoints)):
			for j in range(len(totalPoints)):
				for k in range(len(totalPoints)):
					for l in range(len(totalPoints)):

						distance1 = self.getDistance(totalPoints, i, j)
						distance2 = self.getDistance(totalPoints, k, l)
						distance = distance1+distance2

						if self.validPoints(totalPoints, i, j, k, l) and distance < currentDistance:
							self.log(str(totalPoints[i]) + ' ' + str(totalPoints[j]))
							self.log(str(totalPoints[k]) + ' ' + str(totalPoints[l]))
							currentDistance = distance

		return currentDistance
		
def main():

	aTaleOfThreeCities = ATaleOfThreeCities()
	aTaleOfThreeCities.setSolverMethod(aTaleOfThreeCities.connect)
	#aTaleOfThreeCities.setMode(aTaleOfThreeCities.MODE_DEBUG)
	aTaleOfThreeCities.solve({'a': [[0,0],[0,1],[0,2]], 'b': [[2,1],[3,1]], 'c': [[1,3],[5,28]]}, 3.4142)
	aTaleOfThreeCities.solve({'a': [[4,12],[5,8],[11,9],[21,12],[8,2],[10,3],[3,5],[9,7],[5,10],[6,13]], 'b': [[34,51],[35,33],[36,41],[41,45],[32,48],[39,22],[41,33],[37,51],[39,41],[50,40]], 'c': [[86,10],[75,20],[78,30],[81,40],[89,50],[77,60],[83,70],[88,80],[99,90],[77,100]]}, 50.3234)



if __name__ == '__main__':
	main()
