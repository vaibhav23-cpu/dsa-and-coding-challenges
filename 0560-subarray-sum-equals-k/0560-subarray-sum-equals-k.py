class Solution(object):
    def subarraySum(self, nums, k):
        #sbse pehle ek empty dictionary bnaege fir compare krege array ko current number se agar vo sum 'k' k equal hota h toh usko seen m add krdege or tbtk krege jbtk k or sum dono equal nhi hojate
        seen = {0:1}
        sum_num = 0
        res = 0
        for i in range(len(nums)):
            sum_num+= nums[i]
            need = sum_num - k
            if need in seen:
                res += seen[need]
            seen[sum_num] = seen.get(sum_num,0)+1
        return res
