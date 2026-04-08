class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while end > start:
            while not s[start].isalnum() and start < end:
                start += 1
            while not s[end].isalnum() and end > start:
                end -= 1
            
            if s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1

        return True