def productSum(array, count = 1):
    # Write your code here.
    
    sum = 0
    for item in array:
        if isinstance(item, list):
            sum +=  productSum(item, count + 1)
        else:
            sum += item
    return sum * count


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))