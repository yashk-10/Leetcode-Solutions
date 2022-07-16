class Solution:
    def romanToInt(self, s: str) -> int:
        romans = [["I", 1],["V", 5], ["X", 10], ["L", 50], ["C", 100], ["D", 500], ["M", 1000]]
        output = []
        for i in s:
            for x in range(len(romans)):
                if romans[x][0] == i:
                    output.append(romans[x][1])
                    break
            
        for i in range(len(output)-1):
            if output[i] < output[i+1]:
                output[i] = output[i+1]-output[i]
                output[i+1] = 2000
        
        for i in output:
            if i == 2000:
                output.remove(i)
                
        return sum(output)