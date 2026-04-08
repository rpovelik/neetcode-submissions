class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        start, end = 0, 1
        chars = {s[start] : start}
        max_len = len(chars)

        while end < len(s):
            if s[end] in chars and chars[s[end]] >= start:
                start = max(start, chars[s[end]] + 1)
            chars[s[end]] = end
            end += 1
            max_len = max(max_len, end - start)
        
        return max_len