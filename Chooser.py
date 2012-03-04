'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=407
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
