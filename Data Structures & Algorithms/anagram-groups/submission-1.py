class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(str1, str2):
            from collections import Counter
            return Counter(str1) == Counter(str2)
        
        output = []
        scanned = set()
        for i, string in enumerate(strs):
            if string in scanned:
                continue
            anagrams = [string]
            for idx in range(i+1,len(strs)):
                if is_anagram(string, strs[idx]):
                    anagrams.append(strs[idx])
                    scanned.add(strs[idx])
            output.append(anagrams)
        return output
                
