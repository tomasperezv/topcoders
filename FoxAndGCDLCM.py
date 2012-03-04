# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=11364
'''
import TopCoder

class FoxAndGCDLCM(TopCoder.TopCoder):

	max = 1001

	'''
	Generate all the multiples for A, between A and (self.max-1)
		e.g. A = 3 => [3, 6, 9, 12, 15, 18, ..., 3*i, ..., 3*(self.max-1)]
	'''
	def getMult(self, A):
		aM = []

		for i in range(1, self.max):
			aM.append(A*i)

		return aM

	'''
	Less common multiple, brute force approach
	'''
	def LCM(self, A, B):
		aM = self.getMult(A)
		bM = self.getMult(B)
		for i in range(len(aM)):
			for j in range(len(bM)):
				if aM[i] == bM[j]:
					return aM[i]
		return -1

	'''
	Greatest common divisor
		GCD(A, B) = A*B / LCM(A, B)
	'''
	def GCD(self, A, B, lcm):

		# If we are not specifying the lcm value, calculate it.
		if lcm == None:
			lcm = self.LCM(A, B)

		if lcm <> -1:
			return ((A*B)/lcm)
		else:
			return -1

	'''
	Calculate the min value in the array of possible results.
	'''
	def getMin(self, possible):

		min = self.max
		for i in range(len(possible)):
			if possible[i] < min:
				min = possible[i]
		
		if len(possible) == 0:
			return -1
		else:
			return min

	'''
	Given the values lcm(a,b) and gcd(a,b), return the minimun a+b possible value,
	using a brute force approach, generating all the possible combinations of a and b.
	'''
	def solverMethod(self):

		possible = []
		for i in range(1, self.max):
			for j in range(1, self.max):
				if ( (i*j) == (self.G * self.L) ):
					lcm = self.LCM(i, j)
					gcd = self.GCD(i, j, lcm)
					if gcd == self.G and lcm == self.L:
						possible.append(i+j)

		return self.getMin(possible)

		
def main():
	solver = FoxAndGCDLCM()
	solver.setSolverMethod(solver.solverMethod)
	solver.setMode(FoxAndGCDLCM.MODE_DEBUG)
	solver.solve({'G': 2, 'L': 20}, 14)
	solver.solve({'G': 5, 'L': 8}, -1)
	solver.solve({'G': 1000, 'L': 100}, -1)
	solver.solve({'G': 100, 'L': 1000}, 700)

if __name__ == '__main__':
	main()
