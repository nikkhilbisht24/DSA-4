class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        largest = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt+=1
            else:
                cnt = 0
            largest = max(largest, cnt)
            
        return largest
