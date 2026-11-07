class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1
        for i in reversed(range(len(arr))):
            tmp = arr[i]
            arr[i] = max_so_far
            max_so_far = max(max_so_far, tmp)
        return arr