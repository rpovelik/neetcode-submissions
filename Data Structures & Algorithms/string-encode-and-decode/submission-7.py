class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + '%' + s for s in strs)

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        l = len(s)

        while i < l:
            j = i

            while s[j] != '%':
                j += 1

            substr_len = int(s[i : j])
            j += 1

            answer.append(s[j : j + substr_len])
            i = j + substr_len 

        return answer
