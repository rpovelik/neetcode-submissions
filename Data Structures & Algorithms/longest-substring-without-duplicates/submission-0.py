class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        start, end = 0, 1
        chars = set(s[start])
        max_len = len(chars)

        while end < len(s):
            if s[end] not in chars:
                chars.add(s[end])
                end += 1
                max_len = max(max_len, len(chars))
            else:
                chars.remove(s[start])
                start += 1
        
        return max_len