'''
When people whisper to each other in the TopCoder arena, they type "/msg <username> <message>" (quotes and angle brackets for clarity only). However, TopCoder allows users to have spaces in their names. This leads to some ambiguity in regards to who a whisper is actually addressed to. For examples if a user types in "/msg John Doe hi there", this could interpreted in a number of ways. It could be that the user is trying to send the message "Doe hi there" to a user named "John" or it could be that the message is to a user "John Doe", and has content "hi there".
To figure this out you should take a list of users who are logged in, and determine, of the users that the message could possibly be to, which one has the longest name. It may only be to a user if it starts exactly with "/msg <username> ". That is, "/msg " followed by a single space, followed by the user's handle, followed by another space. Thus, if someone typed in "/msg John Doe hi there" and the people logged in were {"John","John Doe","John Doe h"}, the message could be to either "John Doe" or "John" (but not "John Doe h" because there is not a space following his handle in the typed string). Of those two, "John Doe" has the longer name, so we assume it is to him.
Additionally, all whispering is case insensitive, so "/msg John Doe hi there" will go to the same person as "/MSG jOHN dOE HI THERE".
If there is no user who the message could be to return "user is not logged in" (see examples) If typed does not begin with "/msg " return "not a whisper" (note that there is a space at the end of "/msg ").
Definition

Whisper
Method:
toWhom
Parameters:
String[], String
Returns:
String
Method signature:
String toWhom(String[] usernames, String typed)
-
A double space in typed does not match a single space in usernames. (see examples)
-
When the user is found, the returned case should match the case in usernames. (see examples)
Constraints
-
Each element of usernames will contain only letters ('a'-'z' and 'A'-'Z'), and spaces.
-
usernames will contain between 1 and 50 elements, inclusive.
-
Each element of usernames will have between 1 and 50 characters in length, inclusive.
-
Elements of usernames will not have leading, trailing, or double spaces.
-
No two elements of usernames will be identical, ignoring case.
-
typed will be between 1 and 50 characters, inclusive and will contain only letters ('a'-'z' and 'A'-'Z'), spaces, and slashes ('/').
Examples
0)

{"John","John Doe","John Doe h"}
"/msg John Doe hi there"
Returns: "John Doe"
"John Doe" is longer than "John", and "John Doe h" does not match the typed letters.
1)

{"John","John Doe","John Doe h"}
"/MSG jOHN dOE HI THERE"
Returns: "John Doe"
Note that "/msg", as well as the user's name is case insensitive. Also note that the case of the return matches the usernames parameter, not the typed parameter.
2)

{"writer"}
"writer hi"
Returns: "not a whisper"
This is not a whisper.
3)

{"tester"}
"/msg testerTwo you there"
Returns: "user is not logged in"
There is no one logged in named "testerTwo" or "testerTwo you"
4)

{"lbackstrom"}
"/msg lbackstrom"
Returns: "user is not logged in"
Since, by our definition, a message is only to someone if there is a space following their name, this message is not to lbackstrom. However, it does start with "/msg ", so we don't return "not a whisper". Although it may seems rather strange, by the rules we return "user is not logged in".
5)

{"me"}
"/msg  me hi"
Returns: "user is not logged in"
Again note that, by our strict definition of what it means for a message to be to a user, the double space prevents this message from going to the user "me"
6)

{"abc"}
" /msg abc note the leading space"
Returns: "not a whisper"

7)

{"Wow"}
"/msg Wow "
Returns: "Wow"

8)
{"msg"}
"/msg"
Returns: "not a whisper"
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

