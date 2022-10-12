class Solution(object):
    def majorityElement(self, nums):
        
        count1 = 0
        candidate1 = -1
        count2 = 0
        candidate2 = -1
        
        for i in range(len(nums)):
            if nums[i] == candidate1:
                count1+=1
                
            elif nums[i] == candidate2:
                count2 += 1
                
            elif count1 == 0:
                candidate1 = nums[i]
                count1 = 1
                    
            elif count2 == 0:
                candidate2 = nums[i]
                count2 = 1
            
            else:
                count1-=1
                count2-=1
                
        ans = []
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            if nums[i] == candidate1:
                count1+=1
            elif nums[i] == candidate2:
                count2+=1
                
        if count1 > len(nums)/3:
            ans.append(candidate1)
            
        if count2 > len(nums)/3:
            ans.append(candidate2)
            
        return ans
