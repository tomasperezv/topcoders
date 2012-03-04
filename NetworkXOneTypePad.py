# -*- coding: utf-8 -*-
'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=10846
'''
import TopCoder

class NetworkXOneTimePad(TopCoder.TopCoder):

	plaintexts = None
	ciphertexts = None

	def xor(self, a, b):
		result = ''
		for i in range(len(a)):
			result += str( int(a[i]) ^ int(b[i]) )
		self.log(a + ' xor ' + b + ' = ' + result)
		return result

	def crack(self):
		keys = []
		for i in range(len(self.plaintexts)):
			for j in range(len(self.ciphertexts)):
				result = self.xor(self.plaintexts[i], self.ciphertexts[j])
				if not keys.__contains__(result):
					keys.append(result)
		return len(keys)
		
def main():
	networkXOneTimePad = NetworkXOneTimePad()
	networkXOneTimePad.setSolverMethod(networkXOneTimePad.crack)
	#networkXOneTimePad.setMode(topcoder.MODE_DEBUG)
	networkXOneTimePad.solve({'plaintexts': ["110", "001"], 'ciphertexts': ["101", "010"]}, 2)
	networkXOneTimePad.solve({'plaintexts': ["00", "01", "10", "11"], 'ciphertexts': ["00", "01", "10", "11"]}, 4)
	networkXOneTimePad.solve({'plaintexts': ["000", "111", "010", "101", "110", "001"], 'ciphertexts': ["011", "100"]}, 6)

if __name__ == '__main__':
	main()
