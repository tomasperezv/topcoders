# -*- coding: utf-8 -*-
'''
Problem statement

Toastman has sent Fox Ciel a message consisting entirely of lowercase 'o' and 'x' letters. This message has the interesting property that for any even-length contiguous substring of this message, the number of 'o's will equal the number of 'x's. 

Unfortunately due to the nature of the network, some of the letters in the message can become corrupted. You are given a String message, each character of which is 'o', 'x', or '?'. 'o' or 'x' denotes that the letter in the message is not corrupted and is equal to the corresponding letter. A '?' denotes that the letter at that position is corrupted and might have been either 'o' or 'x'. 

Your job is to replace each of the '?' characters in the input by either 'o' or 'x' such that the resulting message has the interesting property described above, and return that corrected message. It is guaranteed that there will be exactly one such message for the given input.

0)	 "x?x?"
Returns: "xoxo"
Consider the entire message, which is a contiguous substring of the input message of length 4, which is even. It has two 'x's, so it follows that the other two '?' characters must be both 'o'.

1)	"?xo?"
Returns: "oxox"
Consider the first two characters of message. Since it's a contiguous substring of the input message and has a length of 2, which is even, and since it already contains one 'x', the first '?' must be 'o'. Then, by considering the entire message as a contiguous substring of length 4, the last character must be 'x'.

2)	"xo"
Returns: "xo"
Sometimes the message is not corrupted.

3)	"o??x??o"
Returns: "oxoxoxo"

4)	"???????x"
Returns: "oxoxoxox"
'''
import TopCoder

class NetworkXZeroOne(TopCoder.TopCoder):

	def isValid(self, message):
		valid = True
		count = 0
		nO = 0
		nX = 0
		for i in range(len(message)):
			if message[i] == 'o':
				nO+=1
			elif message[i] == 'x':
				nX+=1
			count+=1
			if count > 0 and count % 2 == 0 and nO <> nX:
				valid = False
				break
		self.log('# ' + message + ' is valid? ' + str(valid))
		return valid

	def reconstruct(self, message = None, ini = 0):

		if message == None:
			message = ''

		if ini > len(self.message):
			self.log('ending due length: ' + message)
			return message

		end = len(self.message)
		for i in range(ini, end):
			self.log('checking ' + str(i) + ' ' + str(ini)  )
			if self.message[i] == '?':
				tryX = self.reconstruct(message + 'x', i+1)
				tryO = self.reconstruct(message + 'o', i+1)
				if self.isValid(tryX) :
					message+='x'
					self.log('valid char found ' + message)
					return self.reconstruct(message, i+1) 
				elif self.isValid(tryO):
					message+='o'
					self.log('valid char found ' + message + ' calling for ' + str(i) )
					return self.reconstruct(message, i+1) 
			else:
				self.log('adding ' + self.message[i])
				message+=self.message[i]
		return message
		
def main():
	networkXZeroOne = NetworkXZeroOne()
	networkXZeroOne.setSolverMethod(networkXZeroOne.reconstruct)
	#networkXZeroOne.setMode(networkXZeroOne.MODE_DEBUG)
	networkXZeroOne.solve({'message': 'x?x?'}, 'xoxo')
	networkXZeroOne.solve({'message': '?xo?'}, 'oxox')
	networkXZeroOne.solve({'message': 'xo'}, 'xo')
	networkXZeroOne.solve({'message': 'o??x??o'}, 'oxoxoxo')
	networkXZeroOne.solve({'message': '???????x'}, 'oxoxoxox')

if __name__ == '__main__':
	main()
