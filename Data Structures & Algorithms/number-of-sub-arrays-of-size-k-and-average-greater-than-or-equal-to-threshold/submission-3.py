class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counts = 0
        window_sum = sum(arr[:k-1]) or 0
        l, r = 0, k-1

        while r < len(arr):
            window_sum += arr[r]
            if window_sum/k >= threshold:
                counts += 1
            window_sum -= arr[l]
            l += 1
            r += 1

        return counts
            

            
