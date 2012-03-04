# -*- coding: utf-8 -*-
'''
Problem Statement
    
You are going on a road trip with your family. Your dad has given you a map, and has marked where the family car will have to make turns on it. For example:
String[] map = 
	   {".........R....",
		"..............",
		"...L.....R....",
		"..............",
		"...L.....B...."}
'.' denotes open road, 'R' denotes right turn, 'L' denotes left turn, and 'B' denotes turn around You will keep travelling until you leave the map boundaries or loop forever. 

Assuming you started in the top left hand corner travelling right, in the above example your path would be:
 >>>>>>>>>v....                                 ..............
 .........v....                                 ..............
 ...v<<<<<<....   at this point you hit the B   ..............
 ...v..........   and need to turn around so:   ..............
 ...>>>>>><....                                 ...v<<<<<<....
Note that the turns are always relative to the direction you are going.  Your family has decided that it wants to take the most scenic path possible, in other words, travel to the most number of unique positions on the map. In the above example, starting at the upper left hand corner heading right allowed you to cover these locations:
 xxxxxxxxxx....                 
 .........x....
 ...xxxxxxx.... marks off all of the squares
 ...x.......... the car had traveled to.
 ...xxxxxxx....
The total number of x's (unique locations) is 26. Your job is to find the spot and direction on the map you would have to begin at in order to produce the most scenic trip (greatest number of unique locations touched). You will return the number of unique locations touched on the most scenic trip. In the example above, the trip given is the most scenic one, and thus your method would return 26. If there is a turn symbol in the position where you start it comes into effect immediately. For example: map = {"R...B"} If you started at the leftmost point facing right your path would look like: 
v....
 If you started at the rightmost point facing right your path would look like: 
^<<<<
 For this example your method would return 5. A word of caution: loops can occur in the paths chosen. Regardless of whether there is a loop or not, you will always return the number of unique squares you will touch.
Definition
    
Class:
RoadTrip
Method:
howMany
Parameters:
String[]
Returns:
int
Method signature:
int howMany(String[] map)
(be sure your method is public)
    

Notes
-
The point you choose must be ON the map, and the directions must be one of the four directions: Up, Down, Left, Right
Constraints
-
map must contain between 1 and 30 elements inclusive
-
Each element of map will have length between 1 and 30 inclusive
-
Each element of map will have the same length
-
Each element of map will only consist of letter from the following string (quotes for clarity): "BRL."
Examples
0)


(17, [[4, 3, 'left'], [4, 4, 'down'], [4, 5, 'down'], [4, 6, 'down'], [4, 7, 'down'], [4, 8, 'down'], [4, 9, 'down'], [3, 9, 'up'], [3, 8, 'up'], [3, 7, 'up'], [3, 6, 'up'], [3, 5, 'up'], [3, 4, 'up'], [3, 3, 'up'], [3, 2, 'up'], [3, 1, 'up'], [3, 0, 'up']])


    
{".........R....",
 "..............",
 "...L.....R....",
 "..............",
 "...L.....B...."}
Returns: 26
The first example from the problem statement. Heading right from the top left corner is optimal.
1)

    
{".........R.....R.......",
 ".......................",
 ".........B.............",
 ".......................",
 ".......................",
 "..B......R.....R......B",
 ".......................",
 ".......................",
 ".......................",
 ".........B.....B......."}
Returns: 60

2)

    
{"......................R",
 "R....................R.",
 ".R..................R..",
 "..R................R...",
 "...R..............R....",
 "....R.............R....",
 "...R...............R...",
 "..R.................R..",
 ".R...................R.",
 "R.....................R"}
Returns: 230
Starting right from the top left corner spirals arounds the board
3)

    
{".B.....B"}
Returns: 7
Watch out for loops
4)

    
{"..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 "..............................",
 ".............................."}
Returns: 30
'''
class RoadTrip():

	def moveRight(self, map, i, j, facing):
		if facing == 'left':
			facing = 'top'
			i-=1
		elif facing == 'right':
			facing = 'down'
			i+=1
		elif facing == 'up':
			facing = 'right'
			j+=1
		elif facing == 'down':
			facing = 'left'
			j-=1
		return facing, i, j

	def moveLeft(self, map, i, j, facing):
		if facing == 'left':
			facing = 'down'
			i+=1
		elif facing == 'right':
			facing = 'up'
			i-=1
		elif facing == 'up':
			facing = 'left'
			j-=1
		elif facing == 'down':
			facing = 'right'
			j+=1
		return facing, i, j

	def moveAround(self, map, i, j, facing):
		if facing == 'left':
			facing = 'right'
			j+=1
		elif facing == 'right':
			facing = 'left'
			j-=1
		elif facing == 'up':
			facing = 'down'
			i+=1
		elif facing == 'down':
			facing = 'up'
			i-=1
		return facing, i, j

	def move(self, map, i, j, facing):
		if facing == 'left':
			j-=1
		elif facing == 'right':
			j+=1
		elif facing == 'up':
			i-=1
		elif facing == 'down':
			i+=1
		return facing, i, j

	def isValid(self, map, i, j, visited):
		valid = True
		try:
			pos = map[i][j]
		except IndexError:
			valid = False
		try:
			exists = visited[i,j]
			valid = False
		except KeyError:
			pass

		return valid

	def travel(self, map, i, j, facing):
		end = False
		positions = 0
		visited = {}
		travel = []
		while not end:
			if not self.isValid(map, i, j, visited):
				end = True
			elif i >=0 and j>=0:
				travel.append([i,j,facing])
				positions+=1
				visited[i,j] = 'x'
				if map[i][j] == 'R':
					facing, i, j = self.moveRight(map, i, j, facing)
				elif map[i][j] == 'L':
					facing, i, j = self.moveLeft(map, i, j, facing)
				elif map[i][j] == 'B':
					facing, i, j = self.moveAround(map, i, j, facing)
				elif map[i][j] == '.':
					facing, i, j = self.move(map, i, j, facing)	
			else:
				end = True
		return positions, travel

	def howMany(self, map):
		maxValue = -1
		maxTravel = []
		for i in range(len(map)):
			for j in range(len(map[0])):
				positions1, travel1 = self.travel(map, i, j, 'right')
				positions2, travel2 = self.travel(map, i, j, 'left')
				positions3, travel3 = self.travel(map, i, j, 'up')
				positions4, travel4 = self.travel(map, i, j, 'down')
				if positions1  > maxValue:
					maxValue = positions1
					maxTravel = travel1
				if positions2 > maxValue:
					maxValue = positions2
					maxTravel = travel2
				if positions3  > maxValue:
					maxValue = positions3
					maxTravel = travel3
				if positions4  > maxValue:
					maxValue = positions4
					maxTravel = travel4
		return maxValue, maxTravel

def main():
	roadtrip = RoadTrip()
	print roadtrip.howMany([".........R....", "..............", "...L.....R....", "..............", "...L.....B...."])
	print roadtrip.howMany([".........R.....R.......", ".......................", ".........B.............", ".......................", ".......................", "..B......R.....R......B", ".......................", ".......................", ".......................", ".........B.....B......."])
	print roadtrip.howMany([".B.....B"])

if __name__ == '__main__':
	main()
