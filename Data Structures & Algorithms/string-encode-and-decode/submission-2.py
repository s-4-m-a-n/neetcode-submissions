class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += s+"-"
        return result

    def decode(self, s: str) -> List[str]:
        strs = []
        start_idx = 0
        end_idx = 0
        while end_idx < len(s):
            if s[end_idx] == "-":
                single_s = s[start_idx:end_idx] or ""
                start_idx = end_idx+1
                end_idx +=1
                strs.append(single_s)
            else:
                end_idx += 1
        return strs