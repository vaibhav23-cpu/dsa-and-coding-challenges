class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0]+nums[1]+nums[2]
        for i in range (len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                total = nums[i]+nums[j]+nums[k]
                if abs(target-total) < abs(target-closest):
                    closest = total
                if total == target:
                    return total
                elif total<target:
                    j +=1
                else:
                    k-=1
        return closest
                

