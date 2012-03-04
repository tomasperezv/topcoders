# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=7558
'''
import TopCoder

class AdvertisingAgency(TopCoder.TopCoder):

	BILLBOARDS = 100

	def numberOfRejections(self):
		billboard = {}
		rejections = 0
		for i in range(len(self.requests)):
			request = self.requests[i]
			if billboard.has_key(request):
				rejections += 1
			else:
				billboard[self.requests[i]] = True
			
		return rejections
		
def main():
	solver = AdvertisingAgency()
	solver.setSolverMethod(solver.numberOfRejections)
	solver.setMode(AdvertisingAgency.MODE_DEBUG)

	solver.solve({'requests': [1,2,3]}, 0)

	solver.solve({'requests': [1,1,1]}, 2)

	solver.solve({'requests': [1,2,1,2]}, 2)

	solver.solve({'requests':[100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
	100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
	100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
	100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
	100, 100, 100, 100, 100, 100, 100, 100, 100, 100
	]}, 49)

if __name__ == '__main__':
	main()
