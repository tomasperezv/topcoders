'''
The results of rolling a die a number of times is given.  If one particular
value comes up more than 1/4 of the time, or comes up less than 1/10 of the
time, the die is considered to be loaded (Loaded means weighted in such a way
as to make the die show a particular number more or less often than is
statistically acceptable).  

Given a sample of die rolls, decide whether or not the die is loaded, and if
so, return the numbers that came up too many or too few times.

DEFINITION

Class Name: DiceChecker
Method Name: badValues
Parameters: int[]
Returns: int[]

Method signature: int[] badValues(int[] values)
Be sure your method is public.

TopCoder will ensure the validity of the inputs.  Inputs are valid if all of
the following criteria are met:
 *values has between 1 and 50 elements, inclusive.
 *each element of values is between 1 and 6, inclusive.

Return an int[] that contains the numbers between 1 and 6 (inclusive) that were
in the int[] too few or too many times.

NOTES
 - If the die is not loaded, return an empty int[].
 - Sort the output ascending ( { 1, 2 }, not { 2, 1 } ).

Examples:

values: { 1, 2, 3, 4, 5, 6, 1, 2, 3, 4 }
1 comes up 1/5 of the time.
2 comes up 1/5 of the time.
3 comes up 1/5 of the time.
4 comes up 1/5 of the time.
5 comes up 1/10 of the time.
6 comes up 1/10 of the time.
No value comes up more than 1/4 of the time or less than 1/10 of the time.
The die is not loaded so return {} (empty int[]).

values: { 3, 1, 5 }
1 comes up 1/3 of the time.
2 does not comes up.
3 comes up 1/3 of the time.
4 does not comes up.
5 comes up 1/3 of the time.
6 does not comes up.
2, 4, and 6 come up less than 1/10 of the time, and 1, 2, and 3 come up more
than 1/4 of the time so return { 1, 2, 3, 4, 5, 6 }.

values : { 1, 1, 1, 1, 1, 1, 1, 2, 2, 2 }
1 comes up 7/10 of the time.
2 comes up 3/10 of the time.
3 does not comes up.
4 does not comes up.
5 does not comes up.
6 does not comes up.
All values are out of the range specified for an unloaded die (> 1/4 or < 1/10).
return { 1, 2, 3, 4, 5, 6 }.

values : { 1, 1, 3, 3, 4, 4, 2, 2, 5, 5, 6, 6 }
1 comes up 1/6 of the time.
2 comes up 1/6 of the time.
3 comes up 1/6 of the time.
4 comes up 1/6 of the time.
5 comes up 1/6 of the time.
6 comes up 1/6 of the time.

All values are in the range specified for an unloaded die (> 1/4 or < 1/10)
return {}.
'''
class DiceChecker():
	
	_diceValues = [1,2,3,4,5,6]

	MAX_PROB = float(float(1)/float(4))
	MIN_PROB = float(float(1)/float(10))

	def isTooSmallProb(self, value):
		return value < self.MIN_PROB

	def isTooBigProb(self, value):
		return value > self.MAX_PROB

	def initDictionary(self):
		n = len(self._diceValues)
		dictionary = {}
		for i in range(n):
			dictionary[i+1] = 0
		return dictionary

	def getCardinality(self, values):
		n = len(values)
		probs = self.initDictionary()
		for i in range(n):
			probs[values[i]] += 1
		return probs
	
	def getProbs(self, values):
		probs = {}
		n = len(values)
		cardinality = self.getCardinality(values)
		for i in range(len(self._diceValues)):
			prob = float(cardinality[i+1])
			prob = prob / n
			probs[i+1] = prob 
		return probs

	def badValues(self, values):
		smallBadValues = []
		bigBadValues = []
		n = len(values)
		probs = self.getProbs(values)
		print probs
		for i in range(len(probs)):
			if self.isTooSmallProb(probs[i+1]):
				smallBadValues.append(i+1)
			elif self.isTooBigProb(probs[i+1]):
				bigBadValues.append(i+1)
		return [smallBadValues, bigBadValues]
			
		
def main():
	diceChecker = DiceChecker()
	print diceChecker.badValues([1,2,3,4,5,6,1,2,3,4])
	print diceChecker.badValues([3,1,5])
	print diceChecker.badValues([1, 1, 1, 1, 1, 1, 1, 2, 2, 2])
	print diceChecker.badValues([1, 1, 3, 3, 4, 4, 2, 2, 5, 5, 6, 6])

if __name__ == '__main__':
	main()
