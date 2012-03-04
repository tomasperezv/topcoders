'''
Class Name: SquareDigits
Method Name: smallestResult
Parameters: int
Returns: int

Define the function S(x) as the sum of the squares of the digits of x.   
For example: S(3)=3*3=9 and S(230)=2*2+3*3+0*0=13.

Define the set T(x) to be the set of unique numbers that are produced by
repeatedly applying S to x.  That is: S(x), S(S(x)), S(S(S(x))), etc... 
For example, repeatedly applying S to 37:
S(37)=3*3+7*7=58.  
S(58)=5*5+8*8=89.
S(89)=145.
S(145)=42. 
S(42)=20.
S(20)=4.
S(4)=16.
S(16)=37. 
Note this sequence will repeat so we can stop calculating now and: 
T(37)={58,89,145,42,20,4,16,37}.
However, note T(x) may not necessarily contain x.  

Implement a class SquareDigits, which contains a method smallestResult.  The
method takes an int, n, as a parameter and returns the smallest int, x, such
that T(x) contains n.

The method signature is (be sure your method is public): 
int smallestResult(int n); 

TopCoder will ensure n is non-negative and is between 0 and 199 inclusive.

Examples:
If n=0: S(0) = 0, so T(0)={0}, so the method should return 0.

If n=2: T(0) through T(10) do not contain the value 2.  If x=11, however:
S(11)=1*1+1*1=2, so T(11) contains 2, and the method should return 11.

If n=10: T(0) through T(6) do not contain 10.  If x=7:
S(7)=49.
S(49)=97.
S(97)=130.
S(130)=10.
S(10)=1.
and it starts to repeat... 
so T(7) is {49,97,130,10,1}, which contains 10, and the method should return 7.

n=1 -> x=1 
n=19 -> x=133
n=85 -> x=5
n=112 -> x=2666
Definition

Class:
SquareDigits
Method:
smallestResult
Parameters:
int
Returns:
int
Method signature:
int smallestResult(int param0)
(be sure your method is public)
    
'''
class SquareDigits():
    
    def smallestResult(self, x):
        smallest = -1
        i = 0
        found = False
        max = 1000000
        while not found and i<max:
            i+=1
            t = self.t(i)
            if self.find(t, x) <> -1:
                smallest = i
                found = True
                break
        return smallest
    
    def find(self, l, value):
        pos = -1
        for i in range(len(l)):
            if l[i] == value:
                pos = i
                break
        return pos
    
    def t(self, x):
        t = []
        current = self.s(x)
        while self.find(t, current) == -1:
            t.append(current)
            current = self.s(current)
        return t
    
    def s(self, x):
        digits = self.getDigits(x)
        sum = 0
        for i in range(len(digits)):
            sum+=digits[i]*digits[i]
        return sum
    
    def getBase(self, x):
        base = 0
        rest = x/(10**base)
        while rest > 0:
            base +=1
            rest = x/(10**base)
        base -= 1
        return base
    
    def getDigits(self, x):
        ''' 
            Returns an array containing the digits of the number x
        '''
        digits = []
        base = self.getBase(x)
        rest = x
        while base >= 0:
            digit = rest / (10**base)
            rest = rest % (10**base)
            digits.append(digit)
            base-=1
        digits.reverse()
        return digits

def main():
    squareDigits = SquareDigits()
    print squareDigits.smallestResult(10)
    print squareDigits.smallestResult(19)
    print squareDigits.smallestResult(85)
    print squareDigits.smallestResult(112)

if __name__ == '__main__':
    main()