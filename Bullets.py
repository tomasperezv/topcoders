# -*- coding: utf-8 -*-
'''
Each gun leaves a unique set of scratches, sort of like a fingerprint, on every bullet that fires through its chamber. These scratch marks are used widely in forensic investigations of crime scenes.
Given a list of guns and the scratch marks that they leave, and the scratch marks on a bullet, return the element number (0-based) of the gun which fired the bullet.
In order for a bullet to match the gun, the gun must leave just as many scratches as are on the bullet, with the same intervals between scratches. For example, the scratch marks:
"| |||  |   |"
"| |||  |   |"
match, but
"| |||  |   |"
"||| |  |   |"
do not.
Note that since bullets are round, the scratch marks wrap around. Therefore:
"|| ||| | "
" | || |||"
match (since it's the same scratch marks, only starting at a different location).
If no gun matches the bullet, return -1.
Definition

Class:
Bullets
Method:
match
Parameters:
String[], String
Returns:
int
Method signature:
int match(String[] guns, String bullet)
(be sure your method is public)
    

Notes
-
Gun markings cannot be flipped. That is, "|||| ||| || |" doesn't match "| || ||| ||||".
Constraints
-
guns will contain between 0 and 50 elements, inclusive.
-
each element of guns will have the same length as bullet.
-
bullet will have length between 5 and 50, inclusive.
-
bullet and each element of guns can contain only the pipe character '|' and spaces.
-
at most one gun will match the bullet.
Examples
0)

    
{"| | | |","|| || |"," ||||  "}
"|| || |"
Returns: 1

1)

    
{"|||   |","| | || "}
"||||   "
Returns: 0
Notice that index 0 is the same scratch pattern, just shifted.
2)

    
{"|| || ||","| | | | ","||||||||"}
"||| ||| "
Returns: -1
No gun matches the scratches.
3)

    
{}
"| | | |"
Returns: -1

4)

    
{"|| || ||","| | | | ","||| ||| ","||||||||"}
"|| ||| |"
Returns: 2
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
