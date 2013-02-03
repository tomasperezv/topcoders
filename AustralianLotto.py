# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=1934
'''

import TopCoder

class AustralianLotto(TopCoder.TopCoder):

	def evaluate(self):

		result = [0, 0, 0, 0, 0, 0, 0]

		for i in range(len(self.picks)):
			total = 0
			for j in range(len(self.picks[i])):
				for k in range(len(self.drawing)):
					if self.drawing[k] == self.picks[i][j]:
						total = total + 1
			if total == 0:
				result[0] = result[0] + 1
			else:
				result[total] = result[total] + 1

		return result

def main():
	australianLotto = AustralianLotto()
	australianLotto.setSolverMethod(australianLotto.evaluate)
	australianLotto.setMode(australianLotto.MODE_DEBUG)
	australianLotto.solve({'drawing': [3, 11, 18, 23, 37, 45], 'picks': [[4, 7, 14, 30, 33, 35], [1, 11, 12, 25, 37, 38], [11, 18, 19, 20, 21, 22]]}, [1, 0, 2, 0, 0, 0, 0])
	australianLotto.solve({'drawing': [42,26,33,2,13,14], 'picks': [[13,4,36,42,26,12]]}, [ 0,  0,  0,  1,  0,  0,  0])

if __name__ == '__main__':
	main()
