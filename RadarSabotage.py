# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=11493

Problem Statement
    	The final battle between Feudalia and Banania is nearing. Before Feudalian forces reach the Bananian capital, they must cross a well-watched portion of land of dimensions W x H without getting detected by any of the Bananian radars. There are two walls at the left and right sides of the portion of land which you can consider to be infinitely long. One of those walls connects points (0,0) and (0,H) and the other connects points (W,0) and (W,H).



The locations of the radars are given by int[]s radarX and radarY. Each radar i has a power level that is initially set to radarPower[i]. The power level of a radar is a non-negative integer value equal to its power consumption. If the power level of radar i is P, then its detection radius is P*P, which means that the radar can detect any movement within all points with a distance to (radarX[i], radarY[i]) less than or equal to P*P.



The Feudalian force must find a path to take between the bottom and top sides of the rectangle such that none of the points in the path are within the detection radius of any radar. Formally, the path must be a curve that connects two points (x0, 0) and (x1, H) which does not cross either of the two walls, and for every point (x,y) in the path and a radar i, the distance between (x,y) and the radar must be strictly larger than P*P where P is the power level of the radar.



You are a Feudalian spy with the ability to modify the power level of any radar to any non-negative integer value that is not larger than the radar's original power level. Set the power levels in such way that the Feudalian force can cross the rectangle without being detected. If there are multiple ways to do it, minimize the difference in total power consumption between the initial setup and the final setup so that the sabotage is more difficult to notice. Return the minimum difference in power usage that is required to make the land crossable.
 
Definition
    	
Class:	RadarSabotage
Method:	minimumDifference
Parameters:	int, int, int[], int[], int[]
Returns:	int
Method signature:	int minimumDifference(int W, int H, int[] radarX, int[] radarY, int[] radarPower)
(be sure your method is public)
    
 
Constraints
-	W and H will each be between 3 and 1000, inclusive.
-	radarX will contain between 1 and 30 elements, inclusive.
-	radarX, radarY and radarPower will contain the same number of elements.
-	Each element of radarX will be between 1 and W-1, inclusive.
-	Each element of radarY will be between 1 and H-1, inclusive.
-	Each element of radarPower will be between 1 and 200, inclusive.
-	No two radars will be located at the same point.
 
Examples
0)	
    	
8
20
{4}
{4}
{10}
Returns: 9
There is only one radar initially with a power level of 10. If the power level is changed to 1, the radius of the radar will become 1*1 = 1, and it will be possible to pass. If we only changed the level to 2, the radius would become 4, and it would not be possible to pass:
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
