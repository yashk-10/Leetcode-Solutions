class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join(ch for ch in s if ch.isalnum()).lower()
        if s2 == s2[::-1]:
            return True
        return False