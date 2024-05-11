  
        
array = [5, 4,3, 2,1]


for i in range(len(array)):
    for j in range(len(array) - 1):
        if array[j] > array[j + 1]:
            temp = array[j + 1]
            array[j + 1] = array[j]
            array[j] = temp 
            
print(array)