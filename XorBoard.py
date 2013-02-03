# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=12180
'''

import TopCoder

class XorBoard(TopCoder.TopCoder):
	def count(self):
		'''
			r1 + r2 + ... + rn = RCount
			r1 0 1 ... RCount
			r2 ...
			rn ...
			SUM i=0...n (r[i][j]) = RCount
		'''
		for r in range(self.RCount)

		pass

def main():
	xorBoard = XorBoard()
	xorBoard.setSolverMethod(xorBoard.count)
	xorBoard.solve({'H': 2, 'W': 2, 'RCount': 2, 'CCount': 2, 'S': 4}, 4)
	#xorBoard.solve({'H': 2, 'W': 2, 'RCount': 0, 'CCount': 0, 'S': 1}, 0)
	#xorBoard.solve({'H': 10, 'W': 20, 'RCount': 50, 'CCount': 40, 'S': 200}, 333759825)

if __name__ == '__main__':
	main()
