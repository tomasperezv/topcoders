# -*- coding: utf-8 -*-
'''
Problem Statement
    	Lecette thinks that 5 and 8 are fortunate digits. A positive integer is called a fortunate number if it has only fortunate digits in its decimal representation. 



You are given three int[]s a, b and c. Return that number of fortunate numbers which can be expressed as a[i] + b[j] + c[k] for some indices i, j and k. Note that you must not count the same fortunate number more than once.
 
Definition
    	
Class:	FortunateNumbers
Method:	getFortunate
Parameters:	int[], int[], int[]
Returns:	int
Method signature:	int getFortunate(int[] a, int[] b, int[] c)
(be sure your method is public)
    
 
Constraints
-	a, b and c will each contain between 1 and 50 elements, inclusive.
-	Each element of a, b and c will be between 1 and 30,000, inclusive.
 
Examples
0)	
    	
{ 1, 10, 100 }
{ 3, 53 }
{ 4, 54 }
Returns: 2
We have two fortunate numbers 8 = 1 + 3 + 4 and 58 = 1 + 3 + 54. 58 can be also expressed as 1 + 53 + 4, but you must not count 58 twice.
1)	
    	
{ 47 }
{ 500 }
{ 33 }
Returns: 0
580 is not a fortunate number.
2)	
    	
{ 100, 1, 10, 100, 1, 1 }
{ 3, 53, 53, 53, 53, 53, 53 }
{ 4, 54, 4, 54, 4, 54 }
Returns: 2
3)	
    	
{ 500, 800 }
{ 50, 80 }
{ 5, 8 }
Returns: 8
4)	
    	
{ 30000, 26264 }
{ 30000, 29294 }
{ 30000, 29594 }
Returns: 3

'''
class FortunateDigits():

	fortunates = [5, 8]

	def find(self, list, x):
		isPresent = False
		for i in range(len(list)):
			if list[i] == x:
				isPresent = True
				break
		return isPresent

	def getNumberDigits(self, x):
		ndigits = 1
		div = x / 10
		while div > 0:
			div = div / 10
			ndigits += 1
		return ndigits

	def getDigits(self, x):
		nDigits = self.getNumberDigits(x)
		digits = []
		for i in range(nDigits):
			digit = x / (10 **(nDigits-i-1) )
			digits.append(digit)
			x = x - ((10 **(nDigits-i-1) )*digit)
		return digits

	def isFortunate(self, x):
		isFortunate = True
		digits = self.getDigits(x)
		for i in range(len(digits)):
			if not self.find(self.fortunates, digits[i]):
				isFortunate = False
				break
		return isFortunate

	def getFortunate(self, a, b, c):
		fortunates = []
		for i in range(len(a)):
			for j in range(len(b)):
				for k in range(len(c)):
					sum = a[i]+b[j]+c[k]
					if self.isFortunate(sum) and not self.find(fortunates, sum):
						fortunates.append(sum)
		return len(fortunates)

def main():
	fortunateDigits = FortunateDigits()
	print fortunateDigits.getFortunate([1, 10, 100], [3, 53], [4, 54])
	print fortunateDigits.getFortunate([47], [500], [33])
	print fortunateDigits.getFortunate([100, 1, 10, 100, 1, 1], [3, 53, 53, 53, 53, 53, 53], [4, 54, 4, 54, 4, 54])
	print fortunateDigits.getFortunate([500, 800], [50, 80], [5, 8])

if __name__ == '__main__': 
	main()
