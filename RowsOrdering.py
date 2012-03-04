# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=11114
'''
import TopCoder
import itertools

class RowsOrdering():
	
	MAX_VALUE = 50

	'''
	Returns a list with all the possible rows for a table with M columns and N possible values.
	'''
	def _getRows(self, M, N = 50):
		return list(itertools.product(range(1, N+1), repeat=M))

	def order(self, rows):
		pass

def main():
	topcoder = TopCoder.TopCoder()
	rowsOrdering = RowsOrdering()
	topcoder.solve(rowsOrdering.order, ["bb", "cb", "ca"], 54)
'''
	print rowsOrdering.order(["abcd", "ABCD"], 127553)
	print rowsOrdering.order(["Example", "Problem"], 943877448)
	print rowsOrdering.order(["a", "b", "c", "d", "e", "f", "g"], 28)
	print rowsOrdering.order(["a", "a"], 2)
'''

if __name__ == '__main__':
	main()
