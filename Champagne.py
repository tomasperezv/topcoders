# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=1525
'''
import TopCoder
class Champagne(TopCoder.TopCoder):
	glasses = []
	def buildGlasses(self):
		self.glasses = []
		nGlassesLevel = 1
		currentGlass = 1
		for i in range(self.height):
			self.glasses.append([])
			for j in range(currentGlass, currentGlass+nGlassesLevel):
				self.glasses[i].append(j)
				currentGlass+=1
			nGlassesLevel+=1
	
	def getUnits(self):
		units = []
		unitsAvailable = self.units
		currentLevel = 0
		while (unitsAvailable > 0) and (currentLevel < self.height):
			units.append([])
			glassesLevel = len(self.glasses[currentLevel])
			if currentLevel > 0:
				unitsPerGlass = unitsAvailable/glassesLevel
				for glassPos in range(glassesLevel):
					pass
			else:
				if unitsAvailable >= 2:
					units[0].append((2/2)*100)
					unitsAvailable-=2
				else:
					units[0].append((unitsAvailable)/2)
			currentLevel+=1
		return units
		
	def howMuch(self):
		self.buildGlasses()
		print self.getUnits()

def main():
	champagne = Champagne()
	champagne.setSolverMethod(champagne.howMuch)
	champagne.solve({'height': 1, 'glass': 1, 'units': 1}, 0.5)
	
if __name__ == '__main__':
	main()
