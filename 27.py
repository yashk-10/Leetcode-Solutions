class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for x in nums:
            if x != val:
                nums[count] = x
                count += 1
        return count
                