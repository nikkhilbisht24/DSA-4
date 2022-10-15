def nextPermutation(self, nums):
    # next greater number possible with combinations
    # [1,7,9,9,8,3]
    index1 = -1
    index2 = -1

    for i in range(len(nums)-2, -1, -1):
        if(nums[i] < nums[i+1]):
            index1 = i
            break

    # condition for decending order
    if index1 != -1:                
        for i in range(len(nums)-1, -1, -1):
            if(nums[i] > nums[index1]):
                index2 = i
                break

        # swap index1 and index2
        nums[index1], nums[index2] = nums[index2], nums[index1]

        # reverse everything after index1
        start = index1+1
        end = len(nums)-1

        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]

            start+=1
            end-=1
    else:
        nums.sort()
