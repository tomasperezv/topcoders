# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=4512
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
