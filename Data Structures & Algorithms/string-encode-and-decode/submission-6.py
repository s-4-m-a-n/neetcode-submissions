class Solution:
    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        for s in strs:
            enc_str += str(len(s))+"#"+s
        return enc_str

    def decode(self, s: str) -> List[str]:
        i=0
        strs = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            strs.append(s[i:j])
            i = j
        return strs
