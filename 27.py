class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if val == nums[i]:
                nums.append(nums[i])
                nums.pop(i)
                count += 1
        return count
                