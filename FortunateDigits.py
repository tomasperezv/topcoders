# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=11509
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
