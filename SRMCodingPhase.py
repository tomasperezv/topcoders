# -*- coding: utf-8 -*-
'''
Problem statement
@see http://community.topcoder.com/stat?c=problem_statement&pm=11381


Mr. Dengklek introduced you to an online programming contest called SRM (Special Round Match)! 



You are now in the coding phase of the contest. There are 3 problems in the contest. You have practiced a lot before in practice rooms, so you are sure that you can solve the first problem in skills[0] minutes, the second problem in skills[1] minutes and the third problem is skills[2] minutes. 

You have exactly 75 minutes to solve the problems. Before submitting a solution to a problem, you must first open the problem. If you submit a solution to a problem t minutes after you open the problem, you will receive:
(points[0] - 2t) points for the first problem, or
(points[1] - 4t) points for the second problem, or
(points[2] - 8t) points for the third problem.

In your strategy, you only submit a solution to a problem after you solve the problem. If you don't submit a solution to a problem, you will receive zero points for the problem. 

It is well-known that luck plays an important role in a contest. A fortune-teller told you that you have luck points of luck. You may use these points to decrease the amount of time you need to solve the problems, in minutes. Of course, you don't have to use all the points. Each point is worth one minute per problem. So, if you initially can solve a problem in t minutes, by using x points of luck (where x is a positive integer and 0 < x < t), you can solve the problem in (t - x) minutes (it is impossible to use t or more points of luck on the problem). 

Arrange your strategy in this coding phase. Return the maximum total score you can achieve in this coding phase.
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
