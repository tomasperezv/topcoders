# -*- coding: utf-8 -*-
'''
Problem statement

'''

import TopCoder

class Solver(TopCoder.TopCoder):
	def solverMethod(self):
		pass
		
def main():
	solver = Solver()
	solver.setSolverMethod(solver.solverMethod)
	#solver.setMode(topcoder.MODE_DEBUG)
	solver.solve({'param1': 1, 'param2': []}, 2)

if __name__ == '__main__':
	main()
