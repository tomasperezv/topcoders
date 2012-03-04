# -*- coding: utf-8 -*-
'''
Problem Statement
@see http://community.topcoder.com/stat?c=problem_statement&pm=1144
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
