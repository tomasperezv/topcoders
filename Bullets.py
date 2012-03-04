# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=665
'''
class Bullets():

	def getGunDefinitions(self, initialGunDefinition):
		gunDefinitions = []

		# add the provided gun definition
		gunDefinitions.append(initialGunDefinition)

		# generate the rest of gun definitions
		pos = 1
		while pos < len(initialGunDefinition):
			currentDefinition = initialGunDefinition[pos:len(initialGunDefinition)]
			currentDefinition += initialGunDefinition[0:pos]
			gunDefinitions.append(currentDefinition)			
			pos+=1

		return gunDefinitions

	def find(self, gunDefinitions, bullet):
		pos = -1
		for i in range(len(gunDefinitions)):
			if gunDefinitions[i] == bullet:
				pos = i
				break
		return pos
		
	def match(self, guns, bullet):
		pos = -1
		for i in range(len(guns)):
			gunDefinitions = self.getGunDefinitions(guns[i])
			if self.find(gunDefinitions, bullet) <> -1:
				pos = i
				break
		return pos

def main():
	bullets = Bullets()
	print bullets.match(["| | | |","|| || |"," ||||  "], '|| || |')
	print bullets.match(["|||   |","| | || "], '||||   ')
	print bullets.match(["|| || ||","| | | | ","||||||||"], '||| ||| ')
	print bullets.match([], '| | | |')
	print bullets.match(["|| || ||","| | | | ","||| ||| ","||||||||"], "|| ||| |")

if __name__ == '__main__':
	main()
