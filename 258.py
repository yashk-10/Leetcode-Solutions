class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            if len(str(num)) == 1:
                return num
            x = [*str(num)]
            y = [int(i) for i in x]
            num = sum(y)
            