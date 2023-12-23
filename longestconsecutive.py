def longestConsecutive(nums):

    numberSet = set(nums)
    longest = 0
    length = 0 
    
    for num in nums :
        
        if num-1 not in numberSet:
            length = 0
            while (num + length) in numberSet:
                length+=1
            longest = max(length,longest)
            
    return longest
list1 = [100,4,5,200,1,3,2,101,103,102,
105,104,106,107,108,109,110,111,112,113,114,115,1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

# list1 = [100,4,200,1,3,2]
print(longestConsecutive(list1))
