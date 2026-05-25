class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        for i in s:
            dictS[i] = dictS.get(i, 0) + 1
        
        for j in t:
            dictT[j] = dictT.get(j, 0) + 1
        
        return dictT == dictS