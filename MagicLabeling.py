#!/usr/bin/python2.7
'''
    @author: tom@0x101.com
Statement:
You are given a String[] graph, containing N elements and representing an undirected graph on N vertices. 
The j-th character in the i-th element of graph (which is the same as the i-th character in the j-th element of graph) is 'Y' 
if the i-th and j-th vertices of the graph are connected by an edge, and is 'N' otherwise.
You should label each vertex of the graph with an integer between 1 and M, inclusive, and then label each edge 
with the sum of its end vertices' labels. 

The labeling of vertices is called magic if each edge is labeled with the same integer. 
Two labelings of vertices are considered distinct if there's at least one vertex which has different labels in these labelings. 

Calculate the total count of distinct magic labelings of the given graph. Return this number modulo 1,000,003.
'''
class MagicLabeling():
    
    _adjacencyMatrix = None
    _linkedNodes = []
    _links = []
    _numberOfNodes = 0
    _M = 10
    
    def __init__(self, adjacencyMatrix, M):
        self._adjacencyMatrix = adjacencyMatrix
        self._numberOfNodes = len(self._adjacencyMatrix[0])
        self._M = M
        
    def init(self):
        self.initLinks()
    
    def numberOfNodes(self):
        return len(self._adjacencyMatrix[0])
    
    def find(self, list, value):
        position = -1
        for i in range(len(list)):
            if list[i] == value:
                position = i
                break
        return position
        
    def initLinks(self):
        for i in range(self._numberOfNodes):
            for j in range(self._numberOfNodes):
                if self._adjacencyMatrix[i][j] == 'Y':
                    self._links.append([i,j])
                    if self.find(self._linkedNodes, i) == -1:
                        self._linkedNodes.append(i)
                    if self.find(self._linkedNodes, j) == -1:
                        self._linkedNodes.append(j)

    def count(self):
        nodes = len(self._linkedNodes)
        numberCombinations = self._M ** nodes
        
        A = B = C = 1
        for i in range(numberCombinations):
            for j in range(nodes):
                # Apply the different combinations
                C += 1
                if C > self._M:
                    C= 1
                    B += 1
                if B > self._M:
                    B = 1
                    A += 1
                if A > self._M:
                    A = 1
                    B = 1
                    C = 1
        
    def mark(self, i, j):
        self._adjacencyMatrix[i][j] = 'Y'

def initMatrix(nRows, nColumns, defaultValue = 'N'):
    matrix = []
    for i in range(nRows):
        row = []
        for j in range(nColumns):
            row.append(defaultValue)
        matrix.append(row)
    return matrix

def main():
    input = initMatrix(3, 3)
    
    magicLabeling = MagicLabeling(input, 3)
    magicLabeling.mark(0,1)
    magicLabeling.mark(0,2)
    magicLabeling.mark(1,0)
    magicLabeling.mark(1,2)
    magicLabeling.mark(2,0)
    magicLabeling.mark(2,1)
    
    magicLabeling.init()
    
    print magicLabeling.count()

if  __name__ == '__main__':
    main()