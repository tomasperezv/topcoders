'''
@see http://community.topcoder.com/stat?c=problem_statement&pm=163
   
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
