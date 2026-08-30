class Solution(object):
    def maximumSum(self, arr):
        no_delete = arr[0]
        one_delete = float('-inf')
        ans = arr[0]
        for i in range(1,len(arr)):
            old_no_delete = no_delete
            
            no_delete = max(no_delete + arr[i], arr[i])
            one_delete = max(one_delete+arr[i], old_no_delete)
            ans = max(ans, no_delete, one_delete)
        return ans