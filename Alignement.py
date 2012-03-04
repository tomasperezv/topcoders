# -*- coding: utf-8 -*-
'''
Problem statement

You are given two Strings: A and B. You would like to align these two strings by inserting '-' characters in them so that every character in A lines up with the same character in B \
or with a '-' in B, and vice versa. 

Each maximal sequence of consecutive '-' characters costs x, plus an additional 1 per each '-' character. 

For example, changing "ABC" to "A-B-C" costs x+1+x+1, while changing it to "A--BC" costs x+2. Given, A, B, and x return the minimum cost to align the two strings.
 
Definition
    	
Class:	Alignment
Method:	align
Parameters:	String, String, int
Returns:	int
Method signature:	int align(String A, String B, int x)
(be sure your method is public)
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
