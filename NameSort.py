# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=1336
'''
class NameSort():
	def getLastName(self, name):
		lastName = name.split(' ')
		return lastName[len(lastName)-1]

	def find(self, list, name):
		pos = -1
		for i in range(len(name)):
			if list[i] == name:
				pos = i
				break
		return pos

	def isPrevious(self, list, i, item):
		isPrevious = True
		lastName = self.getLastName(item)
		currentLastName = self.getLastName(list[i])
		maxLen = 0
		if len(currentLastName) >= len(lastName):
			maxLen = len(lastName)
		elif len(lastName) >= len(currentLastName):
			maxLen = len(currentLastName)
			
		for pos in range(maxLen):
			if currentLastName[pos].upper() > lastName[pos].upper() or ((currentLastName[pos].upper() == lastName[pos].upper()) and len(lastName) < len(currentLastName) ):
				isPrevious = False
				break
			elif currentLastName[pos].upper() == lastName[pos].upper() and len(lastName) == len(currentLastName): 
				isPrevious = i > self.find(list, item) 
			elif currentLastName[pos] < lastName[pos]:
				break

		return isPrevious

	def newList(self, list):
		newList = []
		for i in range(len(list)):
			added = False
			for j in range(len(newList)):			
				if self.isPrevious(list, i, newList[j]):
					newList = self.addBefore(newList, j, list[i])
					added = True
					break
			if not added:
				newList.append(list[i])
				
		return newList

	def addBefore(self, list, i, name):
		newList = []
		for pos in range(len(list)):
			if pos == i:
				newList.append(name)
			newList.append(list[pos])
		return newList	

def main():
	nameSort = NameSort()
	print nameSort.newList(["Tom Jones","ADAMS","BOB ADAMS","Tom Jones","STEVE jONeS"])
	print nameSort.newList(["C A R Hoare","Kenny G","A DeForest Hoar","Kenny Gee"])
	print nameSort.newList(["Trudy","Trudy","TRUDY"])
	print nameSort.newList(["Alan","aLan","alAn","alaN","ALan","AlAn","AlaN","aLAn","aLaN","alAN"])
	print nameSort.newList(["tIm JoNeS", "Tim Jones", "tom JoNes", "tim joness", "tiM joneS"])

if __name__ == '__main__':
	main()
