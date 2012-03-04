'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=443
'''
class LetterRange():
	
	NOT_FOUND = -1

	_alphabet = "abcdefghijklmnopqrstuvwxyz"

	def getList(self, text):
		listText = []
		for i in range(len(text)):
			char = text[i]
			if char <> ' ' and self.find(listText, char) == self.NOT_FOUND:
				listText.append(char)
		return listText

	def find(self, text, letter):
		pos = self.NOT_FOUND
		for i in range(len(text)):
			if text[i] == letter:
				pos = i	
				break
		return pos 

	def ranges(self, text):
		ranges = []
		listRanges = self.getListRanges(text)
		for i in range(len(listRanges)):
			if len(listRanges[i]) == 1:
				ranges.append(listRanges[i][0] + ":" + listRanges[i][0])
			else:
				ranges.append(listRanges[i][0] + ":" + listRanges[i][len(listRanges[i])-1])
		return ranges

	def getListRanges(self, text):

		ranges = []

		textElements = self.getList(text)
		alphabet = self.getList(self._alphabet)

		for i in range(len(alphabet)):
			ini = alphabet[i]
			pos = self.find(textElements, ini)
			if pos <> self.NOT_FOUND:
				partRange = []
				partRange.append(ini)
				textElements.pop(pos)
				while i<len(alphabet)-1:
					i+=1
					pos = self.find(textElements, alphabet[i])
					if pos <> self.NOT_FOUND:
						partRange.append(alphabet[i])
						textElements.pop(pos)
					else:
						break
				ranges.append(partRange)	

		return ranges

def main():
	letterRange = LetterRange()
	print letterRange.ranges("")
	print letterRange.ranges("  ")
	print letterRange.ranges("aha")
	print letterRange.ranges("xyzzy")
	print letterRange.ranges("and toto too")
	print letterRange.ranges("topcoder quiz")
	print letterRange.ranges("the quick brown fox jumps over the lazy dog")

if __name__ == '__main__':
	main()
