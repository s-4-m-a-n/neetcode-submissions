class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        longest = 0

        for n in nums:
            if not mp[n]:
                mp[n] = mp[n-1] + mp[n+1] + 1
                mp[n - mp[n-1]] = mp[n]
                mp[n + mp[n+1]] = mp[n]
                longest = max(longest, mp[n])
        return longest