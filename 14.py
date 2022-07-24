class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(min(strs, key=len))):
            for x in range(len(strs)-1):
              if strs[x][:i+1] != strs[x+1][:i+1]:
                return strs[x][:i]
        return min(strs)