# -*- coding: utf-8 -*-
'''
Problem statement

Given a string of parentheses, you must turn it into a well formed string by inserting as few parentheses as possible, at any position (you cannot delete or change any of the existing parentheses).

A well formed string of parentheses is defined by the following rules:

	1) The empty string is well formed.
	2) If s is a well formed string, (s) is a well formed string.
	3) If s and t are well formed strings, their concatenation st is a well formed string.

As examples, "(()())", "" and "(())()" are well formed strings and "())(", "()(" and ")" are malformed strings.
Given a String par of parentheses, return the minimum number of parentheses that need to be inserted to make it into a well formed string.

'''
import TopCoder

class MissingParentheses(TopCoder.TopCoder):

	problems = []

	def recursiveCheck(self, str, origin, end):
		isOk = False

		if origin == end or len(str) == 0:
			isOk = True
		else:
			if str[origin] == '(' and str[end] == ')':
				isOk = self.recursiveCheck(str, origin+1, end-1)
			else:
				self.problems.append((origin, end))

		return isOk

	def remove(self, par, toRemove):
		newStr = str(par)
		for i in range(len(toRemove)):
			index = toRemove[i]

			if len(par) <> len(newStr):
				# Correct the index
				correction = len(par)-len(newStr)
				index -= correction

			newStr = newStr[0:index] + newStr[index+2:]

		return newStr	

	def complexCheck(self, par):

		newStr = str(par)
		isValid = True
		toRemove = []

		while len(par) > 0:
			newStr = str(par)
			toRemove = []
			for i in range(len(par)-1):
				if par[i] == '(' and par[i+1] == ')':
					toRemove.append(i)
			newStr = self.remove(par, toRemove)
			if len(par) == len(newStr):
				isValid = False
				break
			par = str(newStr)

		return isValid
	

	def basicCheck(self, str):
		left = 0
		right = 0

		for i in range(len(str)):
			if str[i] == '(':
				left+=1
			elif str[i] == ')':
				right+=1
		return left, right

	def countCorrections(self):
		count = 0

		if not self.complexCheck(self.par):
			left, right = self.basicCheck(self.par)
			count = abs(left-right)

		return count
		
def main():

	missingParentheses = MissingParentheses()
	missingParentheses.setSolverMethod(missingParentheses.countCorrections)
	missingParentheses.setMode(missingParentheses.MODE_DEBUG)

	missingParentheses.solve({'par': '(()(()'}, 2)
	missingParentheses.solve({'par': '()()(()'}, 1)
	missingParentheses.solve({'par': '(())(()())'}, 0)
	missingParentheses.solve({'par': '())(())((()))))()((())))()())())())()()()'}, 7)

if __name__ == '__main__':
	main()
