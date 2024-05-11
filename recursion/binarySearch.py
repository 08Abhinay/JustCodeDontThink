def binarySearch(array, target):
    # Write your code here.


    def searchHelper(low, high):
        if low > high:
            return -1
        
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif target > array[mid]:
            return searchHelper(mid + 1, high)
        elif target < array[mid]:
            return searchHelper(low, mid - 1)
    

    answer = searchHelper(0, len(array)-1)
    return answer + 1

print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 72))