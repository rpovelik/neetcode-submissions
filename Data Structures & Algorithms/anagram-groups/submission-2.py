class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        
        for s in strs:
            l = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                l[idx] += 1
            key = tuple(l)
            if key not in m:
                m[key] = []
            m[key].append(s)

        return list(m.values())