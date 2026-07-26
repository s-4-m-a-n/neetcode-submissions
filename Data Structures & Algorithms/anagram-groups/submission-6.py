from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)

        for s in strs:
            one_hot = [0] * 26
            for c in s:
                one_hot[ord(c) - ord('a')] += 1
            hash_table[str(one_hot)].append(s)
        return list(hash_table.values())