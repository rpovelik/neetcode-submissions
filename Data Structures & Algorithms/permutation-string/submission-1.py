class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_m = [0] * 26
        window_m = [0] * 26
        for i in range(len(s1)):
            s1_m[ord(s1[i]) - ord('a')] += 1
            window_m[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s1), len(s2)):
            print(window_m)
            if s1_m == window_m:
                return True
            else:
                window_m[ord(s2[i - len(s1)]) - ord('a')] -= 1
                window_m[ord(s2[i]) - ord('a')] += 1
        
        return s1_m == window_m
