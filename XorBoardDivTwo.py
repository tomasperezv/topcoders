# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=12188
'''

import TopCoder

class XorBoardDivTwo(TopCoder.TopCoder):

	def getFlipValue(self, value):
		if value == '1':
			return '0'
		else:
			return '1'

	'''
	Count the number of 1's in the board.
	'''
	def count(self, board):
		total = 0
		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] == '1':
					total = total + 1
		return total

	'''
	Flip values of the board in 2 movements, first the row and then the column.
	'''
	def flip(self, board, row, column):
		# flip row
		for j in range(len(board[row])):
			board[row] = board[row][0:j] + self.getFlipValue(board[row][j]) + board[row][j+1:]

		# flip column
		for i in range(len(board)):
			board[i] = board[i][0:column] + self.getFlipValue(board[i][column]) + board[i][column+1:]

		return board

	'''
	Brute force solution to determine the maximum number of 1's that we can obtain, after
	2 flip movements of the board.
	'''
	def theMax(self):
		maxTotal = -1
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				# flip row i and column j
				board = self.flip(list(self.board), i, j)
				# count and store if needed
				currentCount = self.count(board)
				if currentCount > maxTotal:
					maxTotal = currentCount
		return maxTotal

def main():
	xorBoardDivTwo = XorBoardDivTwo()
	xorBoardDivTwo.setSolverMethod(xorBoardDivTwo.theMax)
	xorBoardDivTwo.setMode(xorBoardDivTwo.MODE_DEBUG)
	xorBoardDivTwo.solve({'board': ['101', '010', '101']}, 9)
	xorBoardDivTwo.solve({'board': ['111', '111', '111']}, 5)
	xorBoardDivTwo.solve({'board': ['0101001', '1101011']}, 9)
	xorBoardDivTwo.solve({'board': ["000", "001", "010", "011", "100", "101", "110", "111"]}, 15)
	xorBoardDivTwo.solve({'board': ["000000000000000000000000", "011111100111111001111110", "010000000100000001000000", "010000000100000001000000", "010000000100000001000000", "011111100111111001111110", "000000100000001000000010", "000000100000001000000010", "000000100000001000000010", "011111100111111001111110", "000000000000000000000000"]}, 105)

if __name__ == '__main__':
	main()
