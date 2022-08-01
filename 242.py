class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sL = []
            for i in s:
                sL.append(i)

            for i in range(len(t)):
                if t[i] in sL:
                    sL.remove(t[i])
                else: 
                    return False
            return True
        else:
            return False