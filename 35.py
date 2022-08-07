class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        while nums[index] != target:
            if target < nums[index] and target > nums[index-1]:
                return index
            index += 1
        return index
            
        