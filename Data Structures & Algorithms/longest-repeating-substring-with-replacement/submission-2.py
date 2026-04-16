class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        res = 0

        maxf = 0
        l = 0
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            maxf = max(freqs[s[r]], maxf)
            
            window_size = r - l + 1
            # Most frequent character shall be in the window at least [len(window) - k] times,
            # as we don't care about K elems
            if not maxf >= (window_size - k):
                freqs[s[l]] -= 1
                l += 1
                continue
            
            res = max(res, window_size)
        
        return res
                