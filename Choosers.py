# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=1125
'''
class Chooser():

	def __init__(self, definition):
		self.orientation = definition[0]
		self.leftChooser = definition[2]
		self.rightChooser = definition[4]	

	def switch(self):
		if self.orientation == 'L':
			self.orientation = 'R'
		else:
			self.orientation = 'L'

class Choosers():
	def length(self, game, start):

		choosers = []
		for i in range(len(game)):
			newChooser = Chooser(game[i])
			choosers.append(newChooser)

		totalLength = 0
		end = False
		currentChooser = choosers[start]
		currentChooserPos = start
		while not end:
			if currentChooser.orientation == 'L':
				nextChooserPos = currentChooser.leftChooser
			elif currentChooser.orientation == 'R':
				nextChooserPos = currentChooser.rightChooser


			if nextChooserPos == 'X':
				totalLength+=1
				end = True
			elif int(nextChooserPos) == currentChooserPos:
				# This case is not completely true
				end = True
			else:
				currentChooser.switch()
				totalLength+=1
				currentChooserPos = int(nextChooserPos)
				currentChooser = choosers[currentChooserPos]

			if totalLength == 0:
				totalLength = -1
			
		return totalLength

def main():
	choosers = Choosers()
	print choosers.length(["L 1 2","R 2 0","L X X"], 0)
	print choosers.length(["L 1 2","R 2 0","L X X"], 2)
	print choosers.length(["L 0 0"], 0)

if __name__ == '__main__':
	main()
