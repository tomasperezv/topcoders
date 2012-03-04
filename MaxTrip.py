# -*- coding: utf-8 -*-
'''
Problem Statement: Max Trip
    	You have won a collection of tickets on luxury cruisers. Each ticket can be used only once, but can be used in either direction between the 2 cities printed on the ticket. Your prize gives you free airfare to any city to start your cruising, and free airfare back home from wherever you finish your cruising.
You love to sail and don't want to waste any of your free tickets. How many additional tickets would you have to buy so that your cruise can use all of your tickets?

Create a class MaxTrip that contains a method minBuy that is given Strings portA and portB and that returns the smallest number of additional tickets that can be purchased to allow you to use all of your free tickets. Each position in portA and portB corresponds to one free ticket, allowing you to travel either way between the cities denoted by the corresponding character in portA and in portB.

 
Definition
    	
Class:	MaxTrip
Method:	minBuy
Parameters:	String, String
Returns:	int
Method signature:	int minBuy(String portA, String portB)
(be sure your method is public)
    
 
Constraints
-	portA will contain between 1 and 50 characters, inclusive.
-	portB will contain the same number of characters as portA.
-	portA and portB will contain only uppercase letters ('A'-'Z').
 
Examples
0)	
    	
"AAX"
"CBY"
Returns: 1
You have 3 free tickets, one between A and C, one between A and B, and one between X and Y. You can use all of these tickets if you purchase one additional ticket. One way is to buy a ticket between C and X. Now your cruise could start at B, go from B to A using your 2nd free ticket, then from A to C using your first free ticket, then from C to X using your purchased ticket, and finally from X to Y using your 3rd free ticket.
1)	
    	
"AAAAA"
"CBXYQ"
Returns: 2
One plan is to cruise from C to A to B to Q (using a purchased ticket) to A to X to A (using a purchased ticket) to Y.
2)	
    	
"AB"
"AB"
Returns: 1
Your 2 free tickets are circle cruises that end at the same port that they debark from. To use both of them, you will need to purchase a ticket that goes between A and B.
'''
class MaxTrip():

	def getPorts(self, portA, portB, pos):
		portA = portA[0:pos] + portA[pos+1:len(portA)]
		portB = portB[0:pos] + portB[pos+1:len(portB)]
		return portA, portB
	
	def relocatePath(self, portA, portB, i, path, before = True):
		newPath = []
		origin = portA[i]
		end = portB[i]	
		for pos in range(len(path)):
			if before and pos == i:
				newPath.append([origin, end])
			newPath.append(path[pos])
			if not before and pos == i:
				newPath.append([origin, end])
		return newPath

	def minBuy(self, portA, portB):
		buy = 0
		path = []
		while len(portA) > 0:
			if len(path) == 0:
				currentOrigin = portA[0]
				currentEnd = portB[0]
				portA, portB = self.getPorts(portA, portB, 0)
				path.append([currentOrigin, currentEnd])
			else:
				found = False
				for i in range(len(portA)):
					for j in range(len(path)):
						if not found:
							if portA[i] == path[j][0] or portB[i] == path[j][0]:
								path = self.relocatePath(portA, portB, i, path)
								portA, portB = self.getPorts(portA, portB, i)
								found = True
							elif portA[i] == path[j][1] or portB[i] == path[j][0]:
								path = self.relocatePath(portA, portB, i, path, False)
								portA, portB = self.getPorts(portA, portB, i)
								found = True
				if not found:
					#this should be improved
					portB += portA[0]
					portA += path[0][0]
					buy+=1
		return buy, path
			
def main():
	maxTrip = MaxTrip()
	print maxTrip.minBuy("AAX", "CBY")
	print maxTrip.minBuy("AAAAA", "CBXYQ")
	#print maxTrip.minBuy("AB", "AB")

if __name__ == '__main__':
	main()
