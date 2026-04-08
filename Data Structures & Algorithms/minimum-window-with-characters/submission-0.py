class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        

        window = {}
        t_freq = {}

        for c in t:
            t_freq[c] = 1 + t_freq.get(c, 0)
        
        l = 0
        have = 0
        need = len(t_freq)
        best_len = float("inf")
        res = [-1, -1]

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in t_freq and window[c] == t_freq[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1

                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if best_len != float("inf") else ""