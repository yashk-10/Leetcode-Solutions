class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            if i not in arr:
                arr.append(i)
            else:
                continue
        
        for i in range(len(arr)):
            nums[i] = arr[i]
        
        return len(arr)