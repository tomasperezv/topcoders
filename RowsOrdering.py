# -*- coding: utf-8 -*-
'''
Problem Statement
You are given a table where each row contains exactly M columns, numbered 0 through M-1. Each value in the table is an integer between 1 and 50, inclusive. Each row of the table is distinct, and the table contains all possible distinct rows. Two rows are considered distinct if there is at least one column where the rows have a different value. Hence, the table contains exactly 50^M rows. 



The rows of the table can be sorted using the following scheme:

	First, for each column, assign a permutation of all the integers between 1 and 50, inclusive. Note that this permutation may differ for each column.

	Next, pick a permutation of all M columns.

	Finally, sort the rows in ascending order. Compare each pair of rows as follows:

	Consider the first column in the permutation chosen in step 2. Compare the values in both rows in this column.
If the values in this column are the same in both rows, check the values in the next column in the permutation instead. Repeat this until the values for the chosen column are different.
The row which contains the value that comes earlier in the permutation chosen in step 1 for this column is considered to be smaller than the other row.
You are given a String[] rows that contains a description of several rows of the table described above. Each element represents a single row and contains exactly M characters. The i-th character in each element represents the value in column i for that row and is one of the following letters:
'a'-'z' corresponds to values 1-26
'A'-'X' corresponds to values 27-50
For each of the given rows, define P as the 1-based index of that row in a table sorted as described above. For any given ordering, where an ordering is defined by the permutations chosen in steps 1 and 2 above, define S as the sum of all P for the given rows. Find the minimum possible value of S and return it modulo 1,000,000,007.
 
Definition
    	
Class:	RowsOrdering
Method:	order
Parameters:	String[]
Returns:	int
Method signature:	int order(String[] rows)
(be sure your method is public)
    
 
Notes
-	The number that you should minimize is the number before the modulo and not after the modulo. That is, 1,000,000,010 is larger than 20 even though 1,000,000,010 modulo 1,000,000,007 = 3 < 20.
-	Duplicate elements are allowed in rows. In case rows contains C > 1 occurrences of a certain row, the value of P for this row must be added towards S for C times (see example 4).
 
Constraints
-	rows will contain between 1 and 50 elements, inclusive.
-	Each element of rows will contain between 1 and 50 characters, inclusive.
-	All the elements of rows will contain the same number of characters.
-	Each character in rows will be either 'a'-'z' or 'A'-'X'.
 
Examples
0)	
    	
{"bb", "cb", "ca"}
Returns: 54
One possible ordering is as follows: 



For the first column, choose the permutation {c, b, ...}.

For the second column, choose the permutation {b, a, ...}.

Then, choose the permutation {1, 0} for the columns. 



The rows will then be indexed as follows: 

"cb" = 1 

"bb" = 2 

... 

"ca" = 51 

"ba" = 52 

... 



The sum is 1+2+51 = 54.
1)	
    	
{"abcd", "ABCD"}
Returns: 127553
Lowercase and uppercase letters are considered distinct.
2)	
    	
{"Example", "Problem"}
Returns: 943877448
3)	
    	
{"a", "b", "c", "d", "e", "f", "g"}
Returns: 28
4)	
    	
{"a", "a"}
Returns: 2
Duplicate elements are allowed. The value of P for each such element should be added towards S separately.
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
