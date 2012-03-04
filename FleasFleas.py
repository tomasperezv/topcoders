# -*- coding: utf-8 -*-
'''
Problem Statement
    
My dog has fleas. I suspect that his fleas have fleas. I suspect that his fleas' fleas have fleas!
Assume that every infested creature (either a dog or a flea) is infested with n fleas and that k of these are themselves infested (with smaller fleas). At each smaller size, n stays the same but k decreases by 5 (but never becomes negative).
For example, suppose that n is 30 and k is originally 7. Then my dog is infested by 30 fleas of which 7 are infested with tiny fleas. Each of those 7 is infested with 30 tiny fleas of which 2 are infested with 30 miniscule fleas. No miniscule flea is infested (since 2-5 is not positive). Calculating the entire population we get 23 uninfested fleas + 7 infested fleas + 196 uninfested tiny fleas + 14 infested tiny fleas + 420 minuscule uninfested fleas = 660 fleas of all sizes.
Create a class FleasFleas that contains method population that takes an int n, the number of full-sized fleas on my dog, and an int k, the number of those that are themselves infested, and returns the total flea population on my dog. If the population is more than 10,000,000 return -1.
Definition
    
Class:
FleasFleas
Method:
population
Parameters:
int, int
Returns:
int
Method signature:
int population(int n, int k)
(be sure your method is public)
    

Constraints
-
n is between 1 and 100 inclusive
-
k is between 0 and n inclusive
Examples
0)

    
30
7
Returns: 660
As described in the Problem Statement
1)

    
100
3
Returns: 400
There are 100 full-sized fleas, 3 of which have 100 tiny fleas each
2)

    
100
100
Returns: -1

3)

    
50
15
Returns: 45800

4)

    
100
0
Returns: 100

5)

    
56
23
Returns: 9970464

6)

    
2
2
Returns: 6

7)

    
5
5
Returns: 30
'''
class FleasFleas():

	def population2(self, n, k):
		totalFleas = n
		previousK = 1
		while k > 0:
			totalFleas += k*previousK*n
			previousK = k
			k = k - 5
		return totalFleas

	def population(self, n, k):
		hasFleas = k
		noFleas = n - k
		totalFleas = hasFleas + noFleas
		k -= 5
		while k > 0:
			total = hasFleas * n
			hasFleas = k * (k+5)
			noFleas = total - hasFleas
			totalFleas += hasFleas + noFleas
			k -= 5
		totalFleas += hasFleas * n
		return totalFleas

def main():
	fleasFleas = FleasFleas()
	print fleasFleas.population(30, 7)
	print fleasFleas.population2(30, 7)
	print fleasFleas.population(100, 100)
	print fleasFleas.population2(100, 100)
	print fleasFleas.population(50, 15)
	print fleasFleas.population2(50, 15)
	print fleasFleas.population(100, 0)
	print fleasFleas.population2(100, 0)

if __name__ == '__main__':
	main()
