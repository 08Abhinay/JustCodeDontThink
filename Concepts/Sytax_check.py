  
        
arr = [1, 2, 3, 4]

for i in range(len(arr)):
    if i > 0:
        print("There are values to the left of index", i)
        break
    else:
        print("No values to the left of index", i)
