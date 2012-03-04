'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=1047
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
