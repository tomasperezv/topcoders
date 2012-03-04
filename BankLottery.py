# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=10988

Problem statement
Most of the local Feudalian banks have started using a lottery system instead of paying interest in the traditional way. It's a less expensive system for the banks, and most people don't seem to notice the difference. One bank's current system works as follows.



After the end of each week, the bank holds a drawing. Each bank account holder is given 1 ticket per dollar in his balance. After all the tickets have been distributed, one ticket is chosen randomly. Every ticket has an equal probability of being chosen. The chosen ticket's owner wins weeklyJackpot dollars, which is immediately added to his balance.



You have just opened an account at the bank and would like to know your expected balance at some point in the future. Somehow, you were able to access the current balances of all the account holders at the bank. These balances are given in the int[] accountBalance. Your initial balance is accountBalance[0], and each of the remaining elements of accountBalance is the balance of another person at the bank. For the purposes of this problem, assume that no transactions other than those caused by the lottery system will occur, and assume that no accounts will be closed or created. Return your expected balance after weekCount weeks.
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
