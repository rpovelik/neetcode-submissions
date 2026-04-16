class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        res = 0

        maxf = 0
        l = 0
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            maxf = max(freqs[s[r]], maxf)
            
            if (r - l + 1 - k) > maxf:
                freqs[s[l]] -= 1
                l += 1
                continue
            
            res = max(res, r - l + 1)
        
        return res
                