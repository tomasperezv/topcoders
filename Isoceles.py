# -*- coding: utf-8 -*-
'''   
Given a list of points return how many unique isoceles right triangles use 3 of those points as corners. An isoceles right triangle has 2 sides of equal length and a single right angle (90 degrees). Two isoceles triangles are unique if they differ by at least one point.
Definition
    
Class:
Isoceles
Method:
howMany
Parameters:
int[], int[]
Returns:
int
Method signature:
int howMany(int[] xs, int[] ys)
(be sure your method is public)
    

Notes
-
xs[K] is the x-coordinate of the Kth point and ys[K] is the y-coordinate of the Kth point
Constraints
-
xs will contain between 3 and 50 elements inclusive
-
ys will contain between 3 and 50 elements inclusive
-
xs and ys will contain the same number of elements
-
Each element of xs will be between -1000000 and 1000000 inclusive
-
Each element of ys will be between -1000000 and 1000000 inclusive
-
There will be no duplicate points
Examples
0)

    
{0,1,2}
{0,10,0}
Returns: 0

1)

    
{0,0,5,5}
{0,5,0,5}
Returns: 4
There are four right isoceles triangles in a square.
2)

    
{-1000000,1000000,0}
{0,0,1000000}
Returns: 1
'''
import math

class Isoceles():

	_used = []

	def hasIso(self, A, B, C):
		a1,a2 = A
		b1,b2 = B
		c1,c2 = C
		x = math.sqrt( (c1-a1)**2 + (c2-a2)**2 )
		y = math.sqrt( (b1-a1)**2 + (b2-a2)**2 )
		z = math.sqrt( (c1-b1)**2 + (c2-b2)**2 )

		hasIso = False
		if x == y or x == z or z == y:
			if x == y and x <> z:
				hasIso = (x/z) == 1
			if y == z and x <> z:
				hasIso = (y/x) == 1
		return hasIso
	
	def used(self, A, B, C):
		used = False
		for i in range(len(self._used)):
			current = self._used[i]
			try:
				if current[A] == 'x' and current[B] == 'x' and current[C] == 'x':
					used = True
			except KeyError:
				pass

		if not used:
			self._used.append({A:'x',B:'x',C:'x'})
		return used
		

	def howMany(self, xs, ys):
		n = 0
		for first in range(len(xs)):
			for second in range(len(xs)):
				for third in range(len(xs)):
					if first <> second and first <> third and second <> third:
						A = xs[first], ys[first]
						B = xs[second], ys[second]
						C = xs[third], ys[third]
						if not self.used(A,B,C) and self.hasIso(A,B,C):
							n += 1
		return n

def main():
	isoceles = Isoceles()
	print isoceles.howMany([0,1,2], [0,10,0])
	print isoceles._used
	print isoceles.howMany([0,0,5,5], [0,5,0,5])
	print isoceles.howMany([-1000000,1000000,0], [0,0,1000000])

if __name__ == '__main__':
	main()
