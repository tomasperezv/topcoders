# -*- coding: utf-8 -*-
'''
Problem Statement
    	One-time pad (patented by Vernam in 1919) is one of the most widely known schemes to encrypt a binary string to achieve confidentiality. This scheme takes a binary string (a string consisting of only the digits 0 and 1) as input and outputs another binary string of the same length. The input is called the plaintext, and the output is called the ciphertext. The scheme uses a key which is another binary string of the same length as the input. The i-th bit of the ciphertext is defined as the XOR of the i-th bit of the plaintext and the key (see the notes for XOR definition). The ciphertext is sent to the receiving party. 



In this problem, we will consider several messages, each of length N, encrypted using a single key of length N. 

We would like to investigate how strong this cipher is. Suppose an adversary manages to find out the content of all the original messages (i.e., the plaintexts) and some of the encrypted messages (i.e., ciphertexts). These messages are given in the String[]s plaintexts and ciphertexts, respectively. Return the number of possible keys that are consistent with this data. The constraints will guarantee that there is at least one such key. A key is consistent if for all members of ciphertexts C, there exists a member of plaintexts P such that when P is encrypted using the specified key, it becomes C.
 
Definition
    	
Class:	NetworkXOneTimePad
Method:	crack
Parameters:	String[], String[]
Returns:	int
Method signature:	int crack(String[] plaintexts, String[] ciphertexts)
(be sure your method is public)


0)	
    	
{"110", "001"}
{"101", "010"}
Returns: 2

Returns: 2
The two possible keys are "011" and "100".
1)	
    	
{"00", "01", "10", "11"}
{"00", "01", "10", "11"}
Returns: 4
2)	
    	
{"01", "10"}
{"00"}
Returns: 2
3)	
    	
{"000", "111", "010", "101", "110", "001"}
{"011", "100"}
Returns: 6
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
