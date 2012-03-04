# -*- coding: utf-8 -*-
'''
Problem Statement
    
An adjacency matrix is one way of representing a graph. The adjacency matrix of a simple graph is a square binary matrix (only 0s and 1s) that always has zeros along its main (upper-left to lower-right) diagonal, and is symmetric (by reflection over the main diagonal). If there is a 1 at row R column C in the matrix then there is an edge between vertex R and vertex C in the corresponding graph.  The binary code of a simple graph is found by forming a binary number using the values in the corresponding matrix. For example:
1)           2)          
0 A B C D      0 A B C
A 0 E F G      A 0 D E  where A - J are variables representing 0 or 1
B E 0 H I      B D 0 F
C F H 0 J      C E F 0  notice matrices are symmetric
D G I J 0
The binary code for 1) is JIHGFEDCBA The binary code for 2) is FEDCBA  As shown above you use digits to the right of the main diagonal proceeding right to left, top to bottom. So if the matrix is:
0 1 1 0      0 A B C
1 0 1 1      A 0 D E
1 1 0 0      B D 0 F
0 1 0 0      C E F 0
The binary code is : FEDCBA = 011011 = 27  Given any adjacency matrix representation of a simple graph you can find a simple graph isomorphic to it by performing the following operation: 1) Exchange rows I and J then 2) Exchange columns I and J  So if you take the matrix and exchange rows 2 and 3, and then exchange columns 2 and 3 you will have a simple graph isomorphic to the initial simple graph. Note that this operation can be performed transitively (i.e. if simple graphs X and Y are isomorphic, and simple graphs Y and Z are isomorphic then simple graphs X and Z are isomorphic). In addition all simple graphs are isomorphic to themselves. Your method will find the lowest binary code and the highest binary code from all of the simple graphs isomorphic to the given simple graph. These are called the minicode and maxicode of the given simple graph respectively.  You will be given an int numVertices representing the number of vertices in the simple graph, and a String[] graph representing the edges in the simple graph. Each element of graph will be formatted as follows(quotes for clarity): "Node1 Node2" where Node1 and Node2 are integers between 0 and numVertices-1 inclusive. This signifies an edge between vertices Node1 and Node2. You will return an int[] with exactly 2 elements, whose first element is the minicode and whose second element is the maxicode of the given simple graph. For example: numVertices = 3 graph = {"0 2","1 0"} The simple graph would look something like:
0 ---- 2
|
|
1
The adjacency matrix looks like:
0 1 1
1 0 0
1 0 0
The possible isomorphisms are:
0 1 0         0 0 1
1 0 1   and   0 0 1
0 1 0         1 1 0
So the binary codes are 011, 101, and 110. The biggest is 110 and the smallest is 011. Your method will return {3,6}.
Definition
    
Class:
Isomorph
Method:
minMaxCode
Parameters:
int, String[]
Returns:
int[]
Method signature:
int[] minMaxCode(int numVertices, String[] graph)
(be sure your method is public)
    

Notes
-
A simple graph is by definition undirected and unweighted containing no self-edges
Constraints
-
graph will contain between 0 and 50 elements inclusive
-
numVertices will be between 2 and 8 inclusive
-
Each element of graph will in the format(quotes for clarity): "Node1 Node2" where Node1 and Node2 are integers between 0 and numVertices-1 inclusive with no leading zeros Node1 is not equal to Node2
-
There will be no repeated edges (i.e. if "2 1" is an element of graph then it cannot contain "2 1" again nor can it contain "1 2"
Examples
0)

    
3
{"0 2","1 0"}
Returns: { 3,  6 }

1)

    
8
{}
Returns: { 0,  0 }

2)

    
8
{"1 2","2 3","3 4","3 5","4 5","4 6","4 7","5 6",
 "5 7","6 7"} 
 Returns: { 321456,  267395200 }

 3)

     
 4
 {"0 1","3 1","2 3","2 1","0 3"}
 Returns: { 31,  62 }

'''
class Isomorph():
	def hasEdge(self, graph, i, j):
		hasEdge = False
		for pos in range(len(graph)):
			arc1 = int(graph[pos][0])
			arc2 = int(graph[pos][2])
			if (i == arc1 and j == arc2) or (i == arc2 and j == arc1):
				hasEdge = True
				break
		return hasEdge
	
	def compare(self, a, b):
		same = True
		for i in range(len(a)):
			for j in range(len(a[0])):
				if a[i][j] <> b[i][j]:
					same = False
					break
		return same
	
	def switchRow(self, a, i, j):
		aux = a
		tmpRow = a[i]
		a[i] = a[j]
		a[j] = tmpRow
		return a
	
	def switchColumn(self, a, i, j):
		aux = a
		for pos in range(len(aux)):
			tmpCol = aux[pos][i]
			aux[pos][i] = aux[pos][j]
			aux[pos][j] = tmpCol
		return aux
	
	def copyMatrix(self, a):
		matrix = []
		for i in range(len(a)):
			matrix.append([])
			for j in range(len(a[0])):
				matrix[i].append(a[i][j])
		return matrix
	
	def getIsomorphism(self, a, x):
		iso = self.copyMatrix(a)
		y = x+1
		iso = self.switchRow(iso, x, y)
		iso = self.switchColumn(iso, x, y)
		return iso
	
	def getIsos(self, a):
		isos = [a]
		notPresent = True
		x = 0
		currentIso = self.getIsomorphism(a, x)
		isos.append(currentIso)
		while notPresent:
			x+=1
			if x > len(a[0])-2:
				notPresent = False
				break
			currentIso = self.getIsomorphism(currentIso, x)
			for i in range(len(isos)):
				if self.compare(currentIso, isos[i]):
					notPresent = False
					break
				else:
					isos.append(currentIso)
		return isos
		
	def getAdjacency(self, numVertices, graph):
		adjacency = []
		for i in range(numVertices):
			adjacency.insert(i, [])
			for j in range(numVertices):
				if i == j:
					value = 0
				elif self.hasEdge(graph, i, j):
					value = 1
				else:
					value = 0
				adjacency[i].insert(j, value)
		return adjacency
	
	def getBinaryCode(self, matrix):
		binaryCode = []
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				if j > i:
					binaryCode.append(matrix[i][j])
		binaryCode.reverse()
		return binaryCode
	
	def getBinaryValue(self, binaryCode):
		value = 0
		for i in range(len(binaryCode)):
			value+=binaryCode[i]*(2**(len(binaryCode)-1-i))
		return value
		
	def minMaxCode(self, numVertices, graph):
		adjacency = self.getAdjacency(numVertices, graph)
		isos = self.getIsos(adjacency)
		max = -1
		min = 1000
		for i in range(len(isos)):
			binaryCode = self.getBinaryCode(isos[i])
			binaryCode = self.getBinaryValue(binaryCode)
			if binaryCode > max:
				max = binaryCode
			if binaryCode < min:
				min = binaryCode
		return min, max

def main():
	isomorph = Isomorph()
	print isomorph.minMaxCode(3, ["0 2", "1 0"])
	print isomorph.minMaxCode(8, [])
	print isomorph.minMaxCode(8, ["1 2","2 3","3 4","3 5","4 5","4 6","4 7","5 6", "5 7","6 7"])
	print isomorph.minMaxCode(4, ["0 1","3 1","2 3","2 1","0 3"])

if __name__ == '__main__':
	main()
