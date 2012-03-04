# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=10988
'''

import TopCoder

class BankLottery(TopCoder.TopCoder):

	def totalIncoming(self, accountBalance, currentWeek):

		total = 0

		if currentWeek <> self.weekCount:
			for i in range(len(accountBalance)):
				newBalance = list(accountBalance)
				newBalance[i]+=self.weeklyJackpot
				self.log(newBalance)

				if currentWeek == self.weekCount-1:
					total += newBalance[0]

				total += self.totalIncoming(newBalance, currentWeek+1)
		return total

	def expectedAmount(self):
		return round(float(self.totalIncoming(self.accountBalance, 0)) / (len(self.accountBalance)**self.weekCount), 2)
	
		
def main():
	bankLottery = BankLottery()
	bankLottery.setSolverMethod(bankLottery.expectedAmount)
	#bankLottery.setMode(bankLottery.MODE_DEBUG)
	bankLottery.solve({'accountBalance': [100, 100], 'weeklyJackpot': 100, 'weekCount': 2}, 200)
	bankLottery.solve({'accountBalance': [2, 2, 2], 'weeklyJackpot': 1, 'weekCount': 2}, 2.67)

if __name__ == '__main__':
	main()
