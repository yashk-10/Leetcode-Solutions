class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashTable = {}
        for i in nums:
            if i not in hashTable.keys():
                hashTable[i] = 1
            else:
                hashTable[i] += 1 
        return max(hashTable, key=hashTable.get)    