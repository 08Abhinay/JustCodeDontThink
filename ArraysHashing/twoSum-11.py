def twoSum( numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    # # brute-force
    # for i in range(len(numbers)):

    #     for j in range(i+1,len(numbers)):
    #         if(numbers[i]+ numbers[j] == target):
    #             return [i,j]
        
    #two-pointer-method
    left = 0 
    right = len(numbers) - 1
    
    while(left<right):
        sum = numbers[left] + numbers[right]
        print(f'The sum is {sum}')
        # if(numbers[right] > target):
        #     right-=1
        #     continue
        
        if(sum > target):
            right-=1
            continue
        if(numbers[left] + numbers[right] == target):
            return [left+1, right+1]
        else:
            left+=1
        
    
print(twoSum([-1,0,-1,2,3,4,5,2],-1))