class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        n = len(arr)
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = largest
            largest  = max(temp, largest)
        return arr


