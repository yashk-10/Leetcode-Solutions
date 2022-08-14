class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numList = []
        for i in str(n):
            numList.append(int(i))
        mult = 1
        for i in numList:
            mult = mult * i
        return mult - sum(numList)