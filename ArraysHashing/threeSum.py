def threeNumberSum(array, targetSum):
    array.sort()
    left = 0 
    right = len(array) - 1 
    
    triplets = []
    
    while(left < right):
        
        
        for currentNum in array:
            if (currentNum + array[left] + array[right] == targetSum):
                triplets.append(sorted([currentNum, array[left], array[right]]))
        if sum > targetSum:
            right -=1
        else:
            left += 1

    return triplets

result = threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)

print(result)
    
    
    
    
    
    
