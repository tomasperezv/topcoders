# -*- coding: utf-8 -*-
'''
Problem Statement
    
This problem involves an elaborate marble maze game. The maze is composed of choosers that look like this:
        Right Oriented                     Left Oriented
           |       |                         |       |                     
           |       |                         |       |
           |       |                         |       |
          / \       \                       /       / \
         /   \       \                     /       /   \
        /     \       \                   /       /     \
       /       O       \                 /       O       \
      /       / \       \               /       / \       \
     /       /   \       \             /       /   \       \            
A marble is put in the top of the chooser. The bar in the middle of the chooser determines whether the marble will leave to the left or the right. After a marble passes through the chooser the bar moves. For example, if a marble enters the right oriented chooser pictured above, it would leave toward the right but, the next marble to pass through would leave toward the left. The exact opposite would hold true for the left oriented chooser pictured above. We can make a game by networking a bunch of choosers together using tubes. For example: game = {"L 1 2","R 2 0","L X X"} This means that chooser 0 begins oriented to the left. Its left path leads to chooser 1, and its right path leads to chooser 2. Chooser 1 begins oriented to the right. Its left path leads to chooser 2, and its right path leads to chooser 0. Chooser 2 begins oriented to the left. Its left and right path both leave the game. If I place a marble in chooser 0 it will pass through 4 choosers before leaving the game (namely 0 then 1 then 0 then 2). Given a network of choosers, and a chooser that we drop the marble into, determine how many choosers the marble will pass through before leaving the game. If it will never leave return -1.  Create a class Choosers that contains the method length, which takes a String[] game, and an int chooser, and returns an int representing how many choosers the marble will pass through before leaving the game. Return -1 if it will never leave.
Definition
    
Class:
Choosers
Method:
length
Parameters:
String[], int
Returns:
int
Method signature:
int length(String[] game, int start)
(be sure your method is public)
    

Constraints
-
game will contain between 1 and 15 elements, inclusive.
-
Each element of game will be formatted as "<dir> <left> <right>" with no extra, leading or trailing spaces, or extra leading 0's.
-
<dir> is either 'L' or 'R'
-
<left> and <right> are each either the character 'X' or integers between 0 and the length of game - 1, inclusive.
Examples
0)

    
{"L 1 2","R 2 0","L X X"}
0
Returns: 4
The marble goes from 0 to 1 to 0 to 2 and then leaves.
1)

    
{"L 1 2","R 2 0","L X X"}
2
Returns: 1
The marble leaves immediately.
2)

    
{"L 0 0"}
0
Returns: -1
Clearly, the marble never leaves.
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
