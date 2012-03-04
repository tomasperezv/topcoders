'''
A lexer (lexical analyzer) is used in compilers to break input text into pieces called tokens. In this problem you will be given a list of valid tokens. For example: tokens ={"ab","aba","A"}  Given a list of valid tokens and an input string your lexer will work as follows: 1) a) If the input doesn't begin with one of the valid tokens, remove the first character from the string. 
b) If the input does begin with a valid token, determine the longest valid token the input starts with and remove it from the string. The removed portion is considered CONSUMED. 2) Repeat 1 until there are no characters left in the input.  The lexer is CASE-SENSITIVE so a token must exactly match the beginning of the string.  Given a list of valid tokens and an input string your method will return a list containing the CONSUMED valid tokens in the order they were CONSUMED. For example: tokens = {"ab","aba","A"} input = "ababbbaAab"  "ab" and "aba" are found at the beginning of the input but "aba" is longest so it is consumed. Now: consumed = {"aba"} input = "bbbaAab"  There are no tokens that start with 'b' so the lexer will remove the first 3 characters from the string. consumed = {"aba"} input = "aAab"  The 'a' doesn't match the token "A" due to CASE-SENSITIVITY. The lexer removes the 'a' from the beginning of the string. consumed = {"aba"} input = "Aab"  The lexer consumes the "A" token. consumed = {"aba","A"} input = "ab"  Finally the lexer consumes the "ab" token and completes the process. consumed = {"aba","A","ab"} input = "" The returned list is {"aba","A","ab"}.  Create a class Lexer that contains the method tokenize, which takes a String[] tokens, and a String input, and returns a String[] in the form specified above.

Lexer
Method:
tokenize
Parameters:
String[], String
Returns:
String[]
Method signature:
String[] tokenize(String[] tokens, String input)
(be sure your method is public)
Constraints
-
tokens will contain between 0 and 50 elements inclusive
-
Each element of tokens will have length between 1 and 50 inclusive
-
Each element of tokens will only consist of letters (A-Z,a-z)
-
input will have length between 0 and 50 inclusive
-
input will only consist of letters (A-Z,a-z)
Examples

0) {"ab","aba","A"}
"ababbbaAab"
Returns: { "aba",
  "A",
  "ab" }
Same as above

1) {"a","a","aa","aaa","aaaa","aaaaa","aa"}
"aaaaaaaaaaaaaaaaaaaaaaaaa"
Returns: { "aaaaa",
  "aaaaa",
  "aaaaa",
  "aaaaa",
  "aaaaa" }
Make sure to use the longest valid starting token

2) {"wow","wo","w"}
"awofwwofowwowowowwwooo"

Returns: { "wo",
  "w",
  "wo",
  "w",
  "wow",
  "wow",
  "w",
  "wo" }

3) {"int","double","long","char","boolean","byte","float"}
"intlongdoublecharintintboolean"
Returns: { "int",
  "long",
  "double",
  "char",
  "int",
  "int",
  "boolean" }

4) {}
"Great"
Returns: { }
No valid tokens, so nothing is CONSUMED
5) {"AbCd","dEfG","GhIj"}
"abCdEfGhIjAbCdEfGhIj"
Returns: { "dEfG",
  "AbCd",
  "GhIj" }
Remember CASE-SENSITIVITY
'''
class Lexer():
	
	_tokens = []
	_availableTokens = []
	_input = ""

	def find(self, input):
		pos = -1
		maxLength = 0
		for i in range(len(self._tokens)):
			if self._availableTokens[i] == input:
				currentLength = len(self._availableTokens[i])
				if currentLength > maxLength:
					pos = i
					maxLength = currentLength
		return pos

	def tokenize(self, tokens, input):
		# set the properties of the Lexer
		self._tokens = tokens
		self._availableTokens = tokens
		self._input = input
		
		consumedTokens = []
		maxTasks = 2
		while len(input) > 0:
			maxTokenPos = -1
			for end in range(len(input)):
				end += 1
				currentInput = input[0:end]
				currentPos = self.find(currentInput) 
				if end == len(input):
					# Check if we found something in the last position
					if (maxTokenPos == -1 and currentPos <> -1) or (currentPos <> -1 and maxTokenPos <> -1 and len(self._tokens[currentPos]) > len(self._tokens[maxTokenPos])):
						#print 'found token at ' + str(currentPos)
						maxTokenPos = currentPos

					newInit = 1
					if maxTokenPos <> -1:
						newInit = len(self._tokens[maxTokenPos])
						#consumedTokens.append(self._availableTokens.pop(maxTokenPos))
						consumedTokens.append(self._availableTokens[maxTokenPos])
					input = input[newInit:len(input)]
					#print '==========================='
					break
				elif (maxTokenPos == -1 and currentPos <> -1) or (currentPos <> -1 and maxTokenPos <> -1 and len(self._tokens[currentPos]) > len(self._tokens[maxTokenPos])):
					maxTokenPos = currentPos
		return consumedTokens

def main():
	lexer = Lexer()
	print lexer.tokenize(["ab","aba","A"], "ababbbaAab")
	print lexer.tokenize(["a","a","aa","aaa","aaaa","aaaaa","aa"], "aaaaaaaaaaaaaaaaaaaaaaaaa")
	print lexer.tokenize(["aaaaa", "aaaaa", "aaaaa", "aaaaa", "aaaaa"], "aaaaaaaaaaaaaaaaaaaaaaaaa")
	print lexer.tokenize(["wow","wo","w"], "awofwwofowwowowowwwooo")
	print lexer.tokenize([], "Great")
	print lexer.tokenize(["int","double","long","char","boolean","byte","float"], "intlongdoublecharintintboolean" )
	print lexer.tokenize(["AbCd","dEfG","GhIj"], "abCdEfGhIjAbCdEfGhIj")

if __name__ == '__main__':
	main()
