# -*- coding: utf-8 -*-
'''
Statement
    
A certain business maintains a list of all its customers' names. The list is arranged in order of importance, with the last customer in the list being the most important. We want to create a new list sorted alphabetically according to customers' last names, but among customers with the same last name we want the more important ones to appear earlier in the new list. Alphabetical order (and equality of last names) should not be case sensitive.
Create a class NameSort that contains a method newList that takes a String[] list of names as input and returns the new sorted list as a String[]. The last name of a customer is defined to be the part of the name following the last space character, or the whole name if it has no space characters. The last name of "Bob E Jones" is "Jones". The last name of "Madona" is "Madona".
The names in the new sorted list should retain the same capitalization as they had in the original list.
Definition
    
Class:
NameSort
Method:
newList
Parameters:
String[]
Returns:
String[]
Method signature:
String[] newList(String[] list)
(be sure your method is public)
    

Constraints
-
list will contain between 1 and 50 elements, inclusive
-
each element of list will contain between 1 and 20 characters, inclusive
-
each character in each element of list will be a space, ' ', or a letter ('A'-'Z' or 'a'-'z')
-
no element of list will contain leading or trailing spaces
-
no element of list will contain two or more adjacent spaces
Examples
0)

    
{"Tom Jones","ADAMS","BOB ADAMS",
"Tom Jones","STEVE jONeS"}
Returns: { "BOB ADAMS",  "ADAMS",  "STEVE jONeS",  "Tom Jones",  "Tom Jones" }
ADAMS comes before JONES. The ADAMS names are listed in reverse order as compared to the original list. Likewise for the JONES names.
1)

    
{"C A R Hoare","Kenny G",
"A DeForest Hoar","Kenny Gee"}
Returns: { "Kenny G",  "Kenny Gee",  "A DeForest Hoar",  "C A R Hoare" }
No two of these names have the same last name. So the final list is the case-insensitive alphabetically ordered by last name version of the original.
2)

    
{"Trudy","Trudy","TRUDY"}
Returns: { "TRUDY",  "Trudy",  "Trudy" }
All three have the same last name. So they are sorted by importance, which corresponds to the reverse order as compared with the original list.
3)

    
{"tIm JoNeS", "Tim Jones", "tom JoNes", "tim joness", "tiM joneS"}
Returns: { "tiM joneS",  "tom JoNes",  "Tim Jones",  "tIm JoNeS",  "tim joness" }

4)

    
{"Alan","aLan","alAn","alaN","ALan","AlAn","AlaN","aLAn","aLaN","alAN"}
Returns: 
{ "alAN",
  "aLaN",
  "aLAn",
  "AlaN",
  "AlAn",
  "ALan",
  "alaN",
  "alAn",
  "aLan",
  "Alan" }

5)

    
{"Al Thompson","Bob Johnson", "John Thompson", "John D Thompson","Bob D Johnson"}
Returns: 
{ "Bob D Johnson",
  "Bob Johnson",
  "John D Thompson",
  "John Thompson",
  "Al Thompson" }
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
