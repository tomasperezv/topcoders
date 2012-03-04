# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=6249
'''

import TopCoder

class Alignment(TopCoder.TopCoder):
	def align(self):
		pass
		
def main():
	solver = Alignment()
	solver.setSolverMethod(solver.align)
	solver.setMode(Alignment.MODE_DEBUG)
	solver.solve({'A': 'ABC', 'B': 'ACE', 'x': 1}, 4)
	solver.solve({'A': 'ABAAAABAA', 'B': 'AAAABAABAAA', 'x': 1}, 7)

if __name__ == '__main__':
	main()
