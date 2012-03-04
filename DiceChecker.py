'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=355
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
