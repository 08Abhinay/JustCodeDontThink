
def threeSum(nums):
    
    nums.sort()
    result = []
    
    for i, num in enumerate(nums):
        if i>0 and nums[i-1]==nums[i]:
            continue
        left, right = i+1, len(nums)-1
        while(left<right):
            sum = nums[left] + nums[right] + num
            if sum > 0:
                right-=1
            elif sum < 0:
                left+=1
            else:
                result.append([nums[left], nums[right], num])
                left+=1
                while(nums[left] == nums[left-1] and left<right):
                    left+=1
    return result

print(threeSum([-1,0,1,2,-1,-4]))
    
