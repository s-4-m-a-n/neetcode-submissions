class Solution:
    def climbStairs(self, n: int) -> int:
        hash_map = {}

        def dfs(curr_step):
            if curr_step in hash_map:
                return hash_map[curr_step]
            
            if curr_step > n:
                return 0

            if curr_step == n:
                return 1

            hash_map[curr_step] = dfs(curr_step+1) + dfs(curr_step+2)
            return hash_map[curr_step]

        return dfs(0)
