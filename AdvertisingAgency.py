# -*- coding: utf-8 -*-
'''
Problem statement
@see http://community.topcoder.com/stat?c=problem_statement&pm=7558

You are working in an advertising agency. There are 100 billboards owned by your agency, numbered from 1 to 100.

You clients send you requests, one after another. Each request is the number of the billboard on which the client would like to place his advertisement.

Initially all billboards are empty. Each time you receive a request, you act as follows. If the corresponding billboard is empty, you satisfy the request and occupy the billboard with the client's advertisement. If the corresponding billboard is occupied, you reject the request.

You are given a int[] requests containing the requests in the order you receive them. Return the number of rejected requests.
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
