# -*- coding: utf-8 -*-
'''    
In 1970 John Conway published a paper outlining how very simple rules could lead to very interesting, complicated behavior. His game was based (very roughly) on how biological organisms work. In his game, Conway put a number of "living" organisms on a two dimensional grid. He then applied four rules to all locations on the grid a number of times. As these rules were repeatedly applied, complex behaviors emerged from these four simple rules.
The four rules were based on the number of "living" organisms that were adjacent to each space in the grid. In his game, he defined two grid spaces to be adjacent if they were immediately next to each other, or diagonal to each other. Thus every space in the grid has 8 other spaces in the grid which are adjacent to it.
The original four rules were as follows. 1) If a grid space is adjacent to less than 2 living organisms, any living organism there dies due to its isolation. 2) If a grid space is adjacent to exactly 2 living organisms, any living organism there stays alive if it was alive. 3) If a grid space is adjacent to exactly 3 living organisms, any living organism there stays alive if it was alive, and if there is no living organism, one is "born" there. 4) If a grid space is adjacent to more than 3 living organisms, any living organism there dies due to over crowding.
For this problem, we would like to be able to specify these rules, rather than hard coding them. Thus, part of the input will be a String which specifies the rules. Each character in the String will be one of three characters: 'D', 'S', 'B'. Each character will indicate the effect of the number of adjacent living organisms equal to its index in the String. Thus, the first character in the String (index = 0) will indicate what should happen to organisms on a grid space with 0 adjacent living organisms. In the String, 'D' indicates that organisms on grid spaces adjacent to the number of living organisms equal to the index of the character will die. 'S' indicates that organisms should remain alive, but not be born. 'B' indicates that an organism should be born if it is not already alive, and continue to live if it was already alive. Thus, the input String corresponding to the above 4 rules would be: "DDSBDDDDD" because organisms die whenever they are adjacent to 0, 1, 4, 5, 6, 7, or 8 other living organisms, remain alive when adjacent to exactly 2 other organisms, and are born when adjacent to exactly 3 other organisms.
Your task is, given an input String[], start, showing the initial locations of living organisms, and a String of rules determine how many living organisms there are after the rules have been applied generations times.
Definition
    
Class:
GameOfLife
Method:
alive
Parameters:
String[], String, int
Returns:
int
Method signature:
int alive(String[] start, String rules, int generations)
(be sure your method is public)
    

Notes
-
In the input String[], start, 'X' represents a live organism, and '.' represents an empty space or dead organism.
-
In calculating the number of living organisms adjacent to a grid location, you should "wrap around". Thus organisms on the far left are adjacent to organisms on the far right, and all four corners are adjacent to each other.
-
Each time the rules are applied, they are applied simultaneously to all grid spaces. Thus, we count how many adjacent organisms there are for every grid space before applying the rules.
Constraints
-
start contains between 1 and 50 elements inclusive, each of which contains between 1 and 50 characters, inclusive.
-
start contains only the characters 'X' and '.'
-
rules contains exactly 9 characters, each of which is 'D', 'S', or 'B'
-
generations is between 0 and 1000, inclusive
-
each element of start contains the same number of characters as each other element of start
Examples
0)

    
{"......"
,"......"
,".XXXX."
,"......"
,"......"}
"DDSBDDDDD"
2
Returns: 6
after 1 application of the rules we have:
{"......",
 "..XX..",
 "..XX..",
 "..XX..",
 "......"}
This is because the grid space that we changed from '.' to 'X' had 3 adjacent 'X's, and by our rules, an organism is born when there are 3 adjacent living organisms. The two 'X's at the ends of the line of 'X's are only adjacent to 1 other 'X', and thus, by the rules, they die.
after 2 application of the rules we have:
{"......",
 "..XX..",
 ".X..X.",
 "..XX..",
 "......"}
Since there are 6 'X's, there are 6 living organisms, thus we return 6.
1)

    
{"XX","XX"}
"DDSBDDDDD"
1
Returns: 0
Because we wrap around edges, every space in the grid is adjacent to 8 living organisms, thus they all die after the first application of the rules.
2)

    
{"........XXX"
,"..........X"
,".........X."
,"..........."
,"..........."
,"..........."
,"..........."
,"..........."
,"..........."
,"..........."
,"..........."}
"DDSBDDDDD"
1000
Returns: 5
The well known glider moves up 1 sqaure and 1 sqaure to the right every 4 generations.
3)

    
{".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,"......................XXX.XX......................"
,".......................X..X......................."
,".......................X..XX......................"
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."
,".................................................."}
"DBDBDBDBD"
16
Returns: 80
The famous replicator rule. If the grid extended infinitely, this rule would make an infinite number of copies of the original pattern! However, because our grid wraps around, the replicator no longer replicates the original pattern after about 16 generations.
4)

    
{"X"}
"BDDDDDDDD"
2
Returns: 1
Note that the 8 squares adjacent to (0,0) are all (0,0)
This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
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
