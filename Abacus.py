# -*- coding: utf-8 -*-
'''
Problem statement
@see http://community.topcoder.com/stat?c=problem_statement&pm=4512

An abacus can be used to do arithmetic. The version that we have has 6 horizontal threads, each with nine beads on it. The beads on each thread are always arranged with just one gap, possibly at one of the ends. However many beads are adjacent and at the right end of the thread is the digit value of the thread. The value on the abacus is read by taking the digits in order from top thread to bottom thread and arranging them from left to right (so the top thread is the one that contains the most significant digit).

Create a class Abacus that contains a method add that is given a String[] original and a number val and that returns a String[] showing the abacus after val has been added to the original abacus.

Both in original and in the return, the String[] will contain exactly 6 elements representing the 6 threads in order from top thread to bottom thread. Each element will contain a lowercase 'o' to represent each bead and three consecutive hyphens '-' to indicate the empty part of the thread. Each element will thus contain exactly 12 characters.

'''
import TopCoder

class Abacus(TopCoder.TopCoder):

	def readDigit(self, thread):
		count = 0
		for bead in reversed(thread):
			if bead == 'o':
				count += 1
			else:
				break
		return count
	
	def readAbacus(self, abacus):
		totalValue = 0
		k = 5

		for i in range(len(abacus)):
			currentDigit = self.readDigit(abacus[i])
			totalValue += (10**(k-i)) * currentDigit

		return totalValue
	
	def getThread(self, digit):
		result = ''
		prefix = 9 - digit

		if prefix > 0:
			for i in range(9-digit):
				result += 'o'

		result += '---'

		for i in range(digit):
			result += 'o'

		return result
	
	def generateAbacus(self, value):
		rest = value
		abacus = []

		for i in reversed(range(6)):
			# Easy method, would be converting to string and iterating
			# But I prefer to do it using maths
			currentDigit = rest/(10**i)
			abacus.append(self.getThread(currentDigit))
			rest = rest % (10**i)

		return abacus
	
	def add(self):
		originalValue = self.readAbacus(self.original)
		return self.generateAbacus(originalValue + self.val)
		
def main():
	solver = Abacus()
	solver.setSolverMethod(solver.add)
	solver.setMode(Abacus.MODE_DEBUG)

	solver.solve({'original': ["ooo---oooooo", "---ooooooooo", "---ooooooooo", "---ooooooooo", "oo---ooooooo", "---ooooooooo"], 'val': 5}, 
	["ooo---oooooo", "---ooooooooo", "---ooooooooo", "---ooooooooo", "o---oooooooo", "ooooo---oooo"])

	solver.solve({'original': ["ooo---oooooo", "---ooooooooo", "---ooooooooo", "---ooooooooo", "oo---ooooooo", "---ooooooooo"], 'val': 21},
	["oo---ooooooo", "ooooooooo---", "ooooooooo---", "ooooooooo---", "ooooooooo---", "ooooooooo---"])

if __name__ == '__main__':
	main()
