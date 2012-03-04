# -*- coding: utf-8 -*-
'''
Problem statement
@see http://community.topcoder.com/stat?c=problem_statement&pm=11415

You are given a int[] divisors containing K elements. Find a positive integer n such that exactly K-1 elements of divisors are exact divisors of n. 
If there are several such numbers n, return the smallest possible one. If no such number n exists, return -1 instead.
 
Definition
    	
Class:	AllButOneDivisor
Method:	getMinimum
Parameters:	int[]
Returns:	int
Method signature:	int getMinimum(int[] divisors)
(be sure your method is public)

'''
import TopCoder

class AllButOneDivisor(TopCoder.TopCoder):
	
	maxValue = 10

	def getMinimum(self):
		minimum = 2000 

		for i in range(2, self.maxValue):
			values = list(self.divisors)

			for k in range(len(values)):
				values[k] = values[k]*i

			for k in range(len(values)):
				currentValue = values[k]
				ndivisors = 0
				for j in range(len(self.divisors)):
					if currentValue % self.divisors[j] == 0:
						ndivisors += 1
				if ndivisors == (len(self.divisors)-1) and minimum > currentValue:
					minimum = currentValue

		if minimum == 2000:
			minimum = -1

		return minimum
				
		
def main():
	solver = AllButOneDivisor()
	solver.setSolverMethod(solver.getMinimum)
	solver.setMode(AllButOneDivisor.MODE_DEBUG)
	solver.solve({'divisors': [2, 3, 5]}, 6)
	solver.solve({'divisors': [2, 4, 3, 9]}, 12)
	solver.solve({'divisors': [3, 2, 6]}, -1)

if __name__ == '__main__':
	main()
