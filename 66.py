class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        # elif digits[-1] == 9 and len(digits) == 1:
        #     digits[0] = 1
        #     digits.append(0)
        else:
            digits[-1] = 0
            digits[-2] += 1
        return digits