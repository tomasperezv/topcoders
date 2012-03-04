# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=4677
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
