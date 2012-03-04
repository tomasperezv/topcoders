# -*- coding: utf-8 -*-
'''    
@see http://community.topcoder.com/stat?c=problem_statement&pm=939
'''
class GameOfLife():

	def isOrganism(self, i, j, dashboard):
		isOrganism = False
		try:
			isOrganism = dashboard[i][j] == 'X'
		except IndexError:
			pass
		return isOrganism

	def getAdjacency(self, i, j, dashboard):
		debug = False
		adjacency = 0
		for row in range(i-1, i+2):
			for column in range(j-1, j+2):
				if (row <> i or column <> j)  and self.isOrganism(row, column, dashboard):
					adjacency+=1

		# We wrap around edges
		#case 1
		if i == 0:
			row = len(dashboard)-1
			for column in range(j-1, j+2):
				if (row <> i or column <> j)  and self.isOrganism(row, column, dashboard):
					adjacency+=1

		# case 2
		if i == len(dashboard)-1:
			row = 0
			for column in range(j-1, j+2):
				if (row <> i or column <> j)  and self.isOrganism(row, column, dashboard):
					adjacency+=1

		# case 3
		if j == 0:
			column = len(dashboard[0])-1
			for row in range(i-1, i+2):
				if (row <> i or column <> j)  and self.isOrganism(row, column, dashboard):
					adjacency+=1

		# case 4
		if j == len(dashboard[0])-1:
			column = 0 
			for row in range(i-1, i+2):
				if (row <> i or column <> j)  and self.isOrganism(row, column, dashboard):
					adjacency+=1

		return adjacency

	def applyRule(self, rule, dashboard):
		i, j, rule = rule[0], rule[1], rule[2]
		ncolumns = len(dashboard[0])
		if rule == 'D':
			row = dashboard[i]
			dashboard[i] = dashboard[i][0:j] + '.' + dashboard[i][j+1:ncolumns]
		elif rule == 'B':
			dashboard[i] = dashboard[i][0:j] + 'X' + dashboard[i][j+1:ncolumns]
		return dashboard 
	
	def countOrganism(self, dashboard):
		organism = 0
		for i in range(len(dashboard)):
			for j in range(len(dashboard[0])):
				if dashboard[i][j] == 'X':
					organism +=1
		return organism
		
	def alive(self, dashboard, rules, generations):
		for i in range(generations):
			pendingRules = []
			for i in range(len(dashboard)):
				for j in range(len(dashboard[0])):
					# Calculate the adjacency
					adjacency = self.getAdjacency(i, j, dashboard)
					# Apply the rule
					try:
						rule = rules[adjacency]
						if adjacency > 0:
							#print i, j, adjacency, ' => ', rule
							pass
						pendingRules.append([i, j, rule])
					except:
						pass
			# apply pending rules before of processing
			for pos in range(len(pendingRules)):
				ruleToApply = pendingRules[pos]
				dashboard = self.applyRule(ruleToApply, dashboard)
		return dashboard, self.countOrganism(dashboard) 

def main():
	gameOfLife = GameOfLife()
	print gameOfLife.alive(["......" ,"......" ,".XXXX." ,"......","......"], "DDSBDDDDD", 2)
	print gameOfLife.alive(["XX","XX"], "DDSBDDDDD", 1)
	#print gameOfLife.alive(["X"], "BDDDDDDDD", 2)

if __name__ == '__main__':
	main()
