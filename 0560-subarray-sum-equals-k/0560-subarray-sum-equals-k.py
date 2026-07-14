class Solution(object):
    def subarraySum(self, nums, k):
        #sbse pehle ek empty dictionary bnaege fir compare krege array ko current number se agar vo sum 'k' k equal hota h toh usko seen m add krdege or tbtk krege jbtk k or sum dono equal nhi hojate
        seen = {0: 1}
        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            need = prefix - k
            if need in seen:
                count += seen[need]
            seen[prefix] = seen.get(prefix, 0)+1
        return count
