class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                    continue
            for j in range(i +1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                k = len(nums)-1
                while l<k:
                    total = nums[i]+nums[j]+nums[k]+nums[l]
                    if total == target:
                        result.append([nums[i], nums[j], nums[l], nums[k]])
                        l +=1
                        k -=1
                        while l < k and nums[l]==nums[l-1]:
                            l+=1
                        while l < k and nums[k]==nums[k + 1]:
                            k -=1
                    elif total < target:
                        l +=1
                    else:
                        k-=1
        return result
