# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=11524
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
