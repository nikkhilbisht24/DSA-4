class Solution(object):
    def maxSubArray(self, nums):
        sum = 0
        max_sum = nums[0]
        
        for num in nums:
            sum = sum + num
            max_sum = max(max_sum, sum)
            
            if sum < 0:
                sum = 0
                
        return max_sum
