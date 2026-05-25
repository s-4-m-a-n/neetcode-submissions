class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictS = {}
        dictT = {}
        for i, j in zip(s, t):
            dictS[i] = dictS.get(i, 0) + 1
            dictT[j] = dictT.get(j, 0) + 1
        return dictT == dictS