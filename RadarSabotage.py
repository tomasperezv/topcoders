# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=11493
'''
import math

class RadarSabotage():

	NO_PATH = 9999999999

	def canBeDetected(self, x, y, radarPower):
		return False

	'''
	@see minimumDifference
	'''
	def canPass(self, currentRadar, radarPower):
		# Can we pass by the currentRadar, with that power?
		canPass = True
		centerX = self.radarX[currentRadar]
		centerY = self.radarY[currentRadar]
		radius = radarPower**radarPower
		for y in range(1, self.H):
			found = False
			for x in range(1, self.W):
				distance = math.sqrt(math.pow(centerX-x, 2) + math.pow(centerY-y, 2))
				if distance > radius:
					# we found a possible path!
					found = True
					break
			if not found:
				canPass = False
		return canPass 

	'''
	TODO: Not taking in account that two radars could cover the same region.
	'''
	def minimumDifference(self, W, H, radarX, radarY, radarPower):
		self.W = W
		self.H = H
		self.radarX = radarX
		self.radarY = radarY
		self.radarPower = radarPower
		totalDiff = 0
		for currentRadar in range(len(radarX)):
			minimumDiff = self.NO_PATH
			powers = range(1, radarPower[currentRadar]+1)
			powers.reverse()
			for power in powers:
				currentDiff = radarPower[currentRadar]-power
				if self.canPass(currentRadar, power):
					minimumDiff = currentDiff
				else:
					#print 'there is no path for the radar ' + str(currentRadar) + ' and the power ' + str(power)
					pass
			if minimumDiff == self.NO_PATH:
				# You can't pass for this radar, never.
				totalDiff = self.NO_PATH
				break
			else:
				# There is a path, increment the sum.
				totalDiff+=minimumDiff
		return totalDiff

def main():
	radarSabotage = RadarSabotage()
	print radarSabotage.minimumDifference(8, 20, [4], [4], [10])

if __name__ == '__main__':
	main()
