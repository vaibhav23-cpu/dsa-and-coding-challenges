class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return len(nums)
        i =2
        j =2
        while j< (len(nums)):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i+=1
            
            j +=1
            
        return i

        