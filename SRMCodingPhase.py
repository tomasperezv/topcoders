# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=11381
'''

import TopCoder

class SRMCodingPhase(TopCoder.TopCoder):

	def isValid(self, luck1, luck2, luck3):
		return luck1+luck2+luck3 <= self.luck and luck1 < self.skills[0] and luck2 < self.skills[1] and luck3 < self.skills[2]

	def getLuck(self, i, luck1, luck2, luck3):
		if i == 0:
			return luck1
		elif i == 1:
			return luck2
		else:
			return luck3

	def count(self, luck1 = 0, luck2 = 0, luck3 = 0):

		costs = [2, 4, 8]
		currentScore = 0

		if self.isValid(luck1, luck2, luck3) or (luck1 == 0 and luck2 == 0 and luck3 == 0):
	
			for i in range(len(self.points)):
				points = self.points[i]
				skills = self.skills[i] - self.getLuck(i, luck1, luck2, luck3)
				cost = costs[i]
				currentScore += points - (cost*skills)

		return currentScore

	def countScore(self):

		totalScore = 0
		totalScore = -1
		luckUsage = []

		if self.luck > 0:
			for luck1 in range(self.luck):
				for luck2 in range(self.luck):
					for luck3 in range(self.luck):
						currentScore = self.count(luck1, luck2, luck3)
							
						if currentScore > totalScore:
							luckUsage = [luck1, luck2, luck3]
							totalScore = currentScore
		else:
			totalScore = self.count()

		self.log(luckUsage)

		return totalScore
		
def main():
	srmCodingPhase = SRMCodingPhase()
	srmCodingPhase.setSolverMethod(srmCodingPhase.countScore)
	srmCodingPhase.setMode(srmCodingPhase.MODE_DEBUG)

	srmCodingPhase.solve({'points': [250, 500, 1000], 'skills': [10, 25, 40], 'luck': 0}, 1310)
	#srmCodingPhase.solve({'points': [300, 600, 900], 'skills': [30, 65, 90], 'luck': 25}, 680)
	srmCodingPhase.solve({'points': [250, 550, 950], 'skills': [10, 25, 40], 'luck': 75}, 1736)

if __name__ == '__main__':
	main()
