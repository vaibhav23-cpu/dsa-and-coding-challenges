class Solution(object):
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr)-k
        while left <  right:
            if x-arr[left] > arr[left + k] - x:
                left +=1
            else:
                right -=1
        return arr[left:left+k]
