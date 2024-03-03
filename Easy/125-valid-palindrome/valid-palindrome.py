class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if x.isalnum()]
        i = 0
        j = len(s) - 1
        while i < len(s):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True