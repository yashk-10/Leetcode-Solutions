class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        numDict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
              '6' : 6, '7' : 7, '8' : 8, '9' : 9}
        out1 = 0
        out2 = 0
        for d in num1:
            out1 = out1 * 10 + numDict[d]
        for d in num2:
            out2 = out2 * 10 + numDict[d]
        
        return str(out1 + out2)