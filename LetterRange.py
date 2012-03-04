'''
A letter range is a set of alphabetically consecutive letters taken from the
lowercase alphabetic characters 'a' through 'z'. The lowest and highest letters
of the range, separated by a colon (the character ':'), are used to represent a
letter range. For example, the range "a:c" represents the consecutive letters
'a', 'b', and 'c'. (quotes are not part of the range). The range "w:z"
represents the letters 'w', 'x', 'y', and 'z'. The range "m:m" respresents the
single letter 'm'.  

Given an input String, return the letter ranges ordered alphabetically by the
low value of each range. Letter ranges contained in the result must represent
the largest possible sequences of increasing consecutive letters found in the
input text. The letters of the input do not have to appear in alphabetical
order. Ignore space characters and duplicate letters contained in the input.
For example, the text "fb xee ac" has three letter ranges, "a:c" (the letters
a, b, and c), "e:f" (the letters e and f) and "x:x" (the letter x). Please
refer to the examples.

DEFINITION
Class: LetterRange
Parameters: String
Returns: String[]
Method signature: String[] ranges(String text);

(be sure your method is public)

TopCoder will ensure the validity of the inputs.  Inputs are valid if all of
the following criteria are met:

* text may only contain lowercase letters (a-z) and the space character, ' '.
* text will contain between 0 and 50 characters, inclusive.

NOTES
- When determining a letter range, please keep in mind that the alphabet ends
with 'z' and does not wrap (i.e. 'a' does not come after 'z'). Since the range
must be increasing you cannot have a range that begins with a letter located
near or at end of the alphabet and ends with a letter at or near the beginning
of the alphabet.

EXAMPLES
(Note that the quote characters are for clarity only.)
E1: "" ==> {}      
E2: "  " ==> {}    
E3: "aha" ==> {"a:a","h:h"}
E4: "xyzzy" ==> {"x:z"}
E5: "and toto too" ==> {"a:a","d:d","n:o","t:t"}
E6: "topcoder quiz" ==> {"c:e","i:i","o:r","t:u","z:z"}
E7: "the quick brown fox jumps over the lazy dog" ==> {"a:z"}
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
