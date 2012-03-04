# -*- coding: utf-8 -*-

'''
Problem Statement
@see http://community.topcoder.com/stat?c=problem_statement&pm=608
'''
class Billboard():
	
	def getLettersDictionary(self, letters):
		dictionary = {}
		for i in range(len(letters)):
			letter = letters[i][0]
			dictionary[letter] = letters[i][1:len(letters[i])]
		return dictionary

	def enlarge(self, message, letters):
		result = []
		dictLetters = self.getLettersDictionary(letters)
		for i in range(5):
			row = ""
			# Traversing by rows
			for j in range(len(message)):
				letter = message[j]
				letterString = dictLetters[letter]
				orig = 5*i + (i+1)
				end = orig+5
				row += letterString[orig:end]
				if j < 4:
					row += '.'
			result.append(row)
		return result

def main():
	billboard = Billboard()
	print billboard.enlarge("TOPCODER", ["T:#####-..#..-..#..-..#..-..#.." ,"O:#####-#...#-#...#-#...#-#####" ,"P:####.-#...#-####.-#....-#...." ,"C:.####-#....-#....-#....-.####" ,"D:####.-#...#-#...#-#...#-####." ,"E:#####-#....-####.-#....-#####" ,"R:####.-#...#-####.-#.#..-#..##"])

	print billboard.enlarge("DOK", ["D:####.-#...#-#...#-#...#-####." ,"O:#####-#...#-#...#-#...#-#####" ,"K:#...#-#..#.-###..-#..#.-#...#"])

	print billboard.enlarge("RANDOMNESS", ["S:##.##-#####-#.#.#-#.#.#-####." ,"N:#####-#####-#####-#####-#####" ,"R:#####-#####-##.##-#####-#####" ,"A:.....-.....-.....-.....-....." ,"D:#.#.#-.#.#.-#.#.#-.#.#.-#.#.#" ,"O:#####-#...#-#.#.#-#...#-#####" ,"E:#....-.#...-..#..-...#.-....#" ,"M:#....-.....-.....-.....-....." ,"X:#...#-.#.#.-..#..-.#.#.-#...#"])



if __name__ == '__main__':
	main()
