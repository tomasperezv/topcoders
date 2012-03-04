# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=11146
'''
import itertools
import TopCoder

class AfraidOfEven(TopCoder.TopCoder):

	MAX_INC = 10

	def posValid(self, seq, i):
		isValid = True
		if i > 0 and i < (len(seq)-1) and not seq[i]-seq[i-1] == seq[i+1]-seq[i]:
			isValid = False
		return isValid

	def isValid(self, seq):
		isValid = True
		for i in range(len(seq)):
			if not self.posValid(seq, i):
				isValid = False
				break
		return isValid	
			
	def restoreProgression(self):

		candidate = list(self.seq)

		combinations = list(itertools.product(range(self.MAX_INC), repeat = len(candidate)))

		self.log('trying ' + str(len(combinations)) + ' combinations...')

		for i in range(len(combinations)):
			for j in range(len(combinations[i])):
				inc = combinations[i][j]
				if inc <> 0:
					candidate[j] = candidate[j] * (2 * inc)
			if self.isValid(candidate):
				self.log(combinations[i])
				break
			candidate = list(self.seq)
						
		return candidate
		
def main():
	solver = AfraidOfEven()
	solver.setSolverMethod(solver.restoreProgression)
	solver.setMode(AfraidOfEven.MODE_DEBUG)
	solver.solve({'seq': [1, 1, 3, 1, 5]}, [1, 2, 3, 4, 5])
	solver.solve({'seq': [9, 7, 5, 3, 1]}, [9, 7, 5, 3, 1])
	solver.solve({'seq': [7, 47, 5, 113, 73, 179, 53]}, [14, 47, 80, 113, 146, 179, 212])


if __name__ == '__main__':
	main()
