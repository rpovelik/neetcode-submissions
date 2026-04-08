class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + '%' + s for s in strs)

    def decode(self, s: str) -> List[str]:
        answer = []
        l, r = 0, 0

        while l < len(s):
            while s[r] != '%':
                r += 1
            sub_l = int(s[l : r])
            r += 1
            answer.append(s[r : r + sub_l])
            r += sub_l
            l = r

        return answer