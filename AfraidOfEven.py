# -*- coding: utf-8 -*-
'''
Problem statement
@see http://community.topcoder.com/stat?c=problem_statement&pm=11146

A sequence of integers a[0], a[1], ..., a[N-1], where N >= 3, is called an arithmetic progression if the difference between any two successive terms in the sequence is a constant. More precisely, it is an arithmetic progression if a[i] - a[i-1] = a[i+1] - a[i] for every integer i such that 0 < i < N-1. 

Sasha and Pasha are students sharing the same room. Once, when Pasha had left the room, Sasha was in a good mood. So he took a piece of chalk and wrote an arithmetic progression on the blackboard. The progression consisted of at least 4 elements, all of which were positive integers. Then Sasha went to class, and Pasha came back. 

Pasha is a very nice person, but there's one problem with him -- he's frightened of even numbers! So, when he returned, he decided to make all the numbers on the board odd. He did this by repeatedly finding an arbitrary even number X, erasing it, and writing X/2 in its place. He continued to perform this step until no even numbers remained. 

Your task is to help Sasha restore the initial progression. You will be given a int[] seq, where the i-th element is the i-th number in the sequence written on the blackboard after Pasha's actions. Return an int[] whose i-th element is the i-th number in a sequence that Sasha could have originally written on the blackboard. The constraints will ensure that at least one such sequence exists. If there are several such sequences, choose the one among them whose int[] representation is lexicographically smallest.
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
