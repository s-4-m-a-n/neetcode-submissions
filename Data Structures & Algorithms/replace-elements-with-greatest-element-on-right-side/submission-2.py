class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = float("-inf")
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > largest:
                largest  = arr[i]
            else:
                arr[i] = largest
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[len(arr)-1] = -1
        return arr


