
def trap( height):
    """
    :type height: List[int]
    :rtype: int
    """
    count = 0 
    left = 0
    right = len(height) - 1
    maxL , maxR = height[left], height[right]
    result = 0 

    while (left < right):
        
        if(maxL < maxR):
            left +=1
            maxL = max(maxL, height[left])
            result += maxL - height[left]
            
        else:
            right-=1
            maxR = max(maxR, height[right])
            result += maxR - height[right]
    return result

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    
        