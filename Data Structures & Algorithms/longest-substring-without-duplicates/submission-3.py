class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        answer = 1
        uniq = [0] * 128

        l, r = 0, 0

        while r < len(s):
            if uniq[ord(s[r]) - ord('a')]:
                uniq[ord(s[l]) - ord('a')] = 0
                l += 1
            else:
                uniq[ord(s[r]) - ord('a')] = 1
                r += 1
                answer = max(answer, r - l)

        return answer