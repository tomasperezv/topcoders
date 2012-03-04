'''
When putting together a problem set, a writer must keep in mind the difficulty
and length of a problem.  A good problem set is one with an easy, a middle, and
a hard problem, but doesn't take too much or too little time to complete.

You will be given an input of three int[].  The first int[] consists of easy
problem times, the second consists of middle problem times, and the third
consists of hard problem times.  Return the number of legal problem set
combinations, where a legal set contains exactly 1 easy, 1 middle and 1 hard
problem, and the total time is between 60 and 75 inclusive.

DEFINITION
Class name: Chooser
Method name: numSets
Parameters: int[], int[], int[]
Returns: int
The method signature is:
int numSets(int[] easy, int[] middle, int[] hard)
Be sure your method is public.

TopCoder will ensure the following:
*Each int[] will contain between 0 and 10 elements, inclusive.
*Each element of easy will be an int between 5 and 15, inclusive.
*Each element of middle will be an int between 15 and 45, inclusive.
*Each element of hard will be an int between 30 and 55, inclusive.

EXAMPLES
{5,10,15}
{15,25}
{45}
There are 3*2*1=6 possible sets.  However, since 10+25+45=80 and 15+25+45=85,
two of the sets are illegal, so the method returns 4.

{5,5,5}
{15,15,15}
{45,45,45}
There are 3*3*3=27 possible sets, all legal.  The return value is 27.

{5,5,5}
{15,15,15}
{45,45,35}
There are 27 possible sets again, but for this input any set with the 35 minute
hard problem is too short.  Therefore there are only 3*3*2=18 legal sets, and
the return value is 18.

{}
{15,25}
{30,35,40}
Since there are no easy problems, there are no legal problem sets.  The return
value is 0.
Class:
Chooser
Method:
numSets
Parameters:
int[], int[], int[]
Returns:
int
Method signature:
int numSets(int[] param0, int[] param1, int[] param2)
'''
class Chooser():
	__MAX_TIME_SET = 75

	def hardValid(self, x): 
		return x >= 40 and x <= 55

	def easyValid(self, x):
		return x>=5 and x<=15
	
	def middleValid(self, x):
		return x>=15 and x<=45

	def numSets(self, easy, middle, hard):
		legalSets = []
		for i in range(len(easy)):
			if self.easyValid(easy[i]) and (easy[i] + min(middle)) <= self.__MAX_TIME_SET:
				for j in range(len(middle)):
					if self.middleValid(middle[j]) and (easy[i] + middle[j] + min(hard)) <= self.__MAX_TIME_SET:
						for k in range(len(hard)):
							if self.hardValid(hard[k]) and easy[i]+middle[j]+hard[k] <= self.__MAX_TIME_SET:
								legalSets.append([easy[i], middle[j], hard[k]])
		return len(legalSets)

def main():
	chooser = Chooser()

	easy = [5,10,15]
	middle = [15,25]
	hard = [45]
	print chooser.numSets(easy, middle, hard)

	easy = [5,5,5]
	middle = [15,15,15]
	hard = [45,45,45]
	print chooser.numSets(easy, middle, hard)

	easy = [5,5,5]
	middle = [15,15,15]
	hard = [45,45,35]
	print chooser.numSets(easy, middle, hard)

	easy = []
	middle = [15,25]
	hard = [30,35,40]
	print chooser.numSets(easy, middle, hard)

if __name__ == '__main__':
	main()
