class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_m = [0] * 26
        window_m = [0] * 26
        for i in range(len(s1)):
            s1_m[ord(s1[i]) - ord('a')] += 1
            window_m[ord(s2[i]) - ord('a')] += 1

        eq = 0
        for i in range(26):
            eq += s1_m[i] == window_m[i]

        for i in range(len(s1), len(s2)):
            if eq == 26:
                return True

            idx = ord(s2[i - len(s1)]) - ord('a')
            window_m[idx] -= 1
            if window_m[idx] == s1_m[idx]:
                eq += 1
            elif window_m[idx] + 1 == s1_m[idx]:
                eq -= 1

            idx = ord(s2[i]) - ord('a')
            window_m[idx] += 1
            if window_m[idx] == s1_m[idx]:
                eq += 1
            elif window_m[idx] - 1 == s1_m[idx]:
                eq -= 1
        
        return eq == 26
