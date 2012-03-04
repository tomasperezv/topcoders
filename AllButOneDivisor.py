# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=11415
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
