'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=1147
'''
class Whisper():

	NOT_A_WHISPER = 'not a whisper'
	USER_NOT_LOGGED_IN = 'user is not logged in'
	MSG = '/msg '

	def find(self, usernames, text):
		pos = -1
		maxLenPos = -1
		for i in range(len(usernames)):
			currentUsername = usernames[i]
			if currentUsername.lower()== text.lower() and (maxLenPos == -1 or len(currentUsername) > len(usernames[maxLenPos])):
				maxLenPos = i
		return maxLenPos
	
	def isWhisper(self, text):
		return text[0:len(self.MSG)].lower() == self.MSG.lower()

	def toWhom(self, usernames, types):
		if not self.isWhisper(types):
			return self.NOT_A_WHISPER
		else:
			# remove the initial whisper string
			types = types[len(self.MSG):len(types)]
			# remove each word separated by spaces
			maxUser = -1

			currentText = ''
			i = 0
			while i < len(types):
				if types[i] == ' ':
					currentText = types[0:i]
					currentUser = self.find(usernames, currentText)
					if currentUser <> -1 and (maxUser == -1 or (len(usernames[maxUser]) < len(usernames[currentUser]) ) ):
						maxUser = currentUser
				i+=1

			if maxUser == -1:
				return self.USER_NOT_LOGGED_IN
			else:
				return usernames[maxUser]

def main():

	whisper = Whisper()
	print whisper.toWhom(["John","John Doe","John Doe h"], "/msg John Doe hi there")
	print whisper.toWhom(["John","John Doe","John Doe h"], "/MSG jOHN dOE HI THERE")
	print whisper.toWhom(["writer"], "writer hi")
	print whisper.toWhom(["tester"], "/msg testerTwo you there")
	print whisper.toWhom(["lbackstrom"], "/msg lbackstrom")
	print whisper.toWhom(["me"], "/msg  me hi")
	print whisper.toWhom(["abc"], " /msg abc note the leading space")
	print whisper.toWhom(["Wow"], "/msg Wow ")
	print whisper.toWhom(["msg"], "/msg")

if __name__ == '__main__':
	main()

