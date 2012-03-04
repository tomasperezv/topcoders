# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=1165
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
