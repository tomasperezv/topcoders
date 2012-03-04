# -*- coding: utf-8 -*-
class TopCoder():
	
	MODE_DEBUG = 0
	MODE_DEFAULT = 1

	solverMethod = None

	def __init__(self):
		self._mode = self.MODE_DEFAULT
	
	def setSolverMethod(self, solverMethod):
		self.solverMethod = solverMethod

	def setMode(self, mode = 1):
		self._mode = mode

	def log(self, str):
		if (self._mode == self.MODE_DEBUG):
			print str

	def isDebugActive(self):
		return self._mode == self.MODE_DEBUG

	def setProperties(self, params):
		for k, v in params.iteritems():
			setattr(self, k, v)

	def solve(self, params, expected):
		# Apply the params as methods
		self.setProperties(params)
		
		result = self.solverMethod()

		if result == expected:
			print '* "' + str(result) + '"\tOk.'
		else:
			print '# Error, obtained: "' + str(result) + '"\texpected: ' + str(expected)
