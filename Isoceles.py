# -*- coding: utf-8 -*-
'''   
@see http://community.topcoder.com/stat?c=problem_statement&pm=1169
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
