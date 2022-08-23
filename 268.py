class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(nums+1):
            if i not in nums:
                return i