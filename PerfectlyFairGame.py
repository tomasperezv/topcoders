# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=11530
'''

import TopCoder

class PerfectlyFairGame(TopCoder.TopCoder):

	def getZeros(self, n):
		str = ''
		for i in range(n):
			str += '0'
		return str

	def buildBoard(self):
		# For N x M the real possiblity board is N+2 x M+2
		board = []
		N = len(self.board)
		M = len(self.board[0])

		board.append(self.getZeros(M+2))

		for i in range(N):
			newRow = '0' + self.board[i] + '0'
			board.append(newRow)

		board.append(self.getZeros(M+2))

		return board
			

	def winChance(self):
		# Generate the new board
		board = self.buildBoard()

		N = len(board)
		M = len(board[0])

		total = 0
		totalWins1 = 0
		totalWins2 = 0

		for i in range(self.darts):
			for i1 in range(N):
				for j1 in range(M):
					for i2 in range(N):
						for j2 in range(M):
							total += 1
							if board[i1][j1] < board[i2][j2]:
								totalWins2 += 1
							elif board[i1][j1] > board[i2][j2]:
								totalWins1 += 1

		self.log(totalWins1)
		self.log(totalWins2)
		return float(totalWins2)/float(total)
		
def main():
	solver = PerfectlyFairGame()
	solver.setSolverMethod(solver.winChance)
	solver.setMode(solver.MODE_DEBUG)
	solver.solve({'board': ["123", "456", "789"], 'darts': 10}, 0.5)
	solver.solve({'board': ["55555", "55555", "55555", "55555", "55555"], 'darts': 20}, 0.5)
	solver.solve({'board': ["0909", "9090", "0909", "9090"], 'darts': 20}, 0.5)
	solver.solve({'board': ["888","808","888","000","000","999","999"], 'darts': 1}, 0.537037037037037)

if __name__ == '__main__':
	main()
