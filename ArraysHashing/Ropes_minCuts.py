def unitCut(n):
    if n == 1:
        return 0  # No cuts needed for a 1-inch rope
    
    cuts = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2  # Halve the rope
        else:
            n = (n // 2) + 1  # Cut the rope in half and add one to the length
        cuts += 1
    
    return cuts

def recursiveCuts(n):
    if n == 1:
        return 0  # No cuts needed for a 1-inch rope
    
    if n % 2 == 0:
        return 1 + recursiveCuts(n // 2)  # Add 1 for the current cut and recurse on the halved rope
    else:
        return 2 + recursiveCuts(n // 2) + recursiveCuts((n // 2) + 1)  # Add 2 for the current cut and recurse on the halved ropes

import math
 
# Function to return the
# minimum time required
# to split stick of N into
# length into unit pieces
def min_time_to_cut(N):
     
    if (N == 0):
        return 0
         
    # Return the minimum
    # unit of time required
    return int(math.log2(N)) + 1
 
# Driver Code
N = 100
 
print(min_time_to_cut(N))
 


# Example usage:
n =50000
# cuts = recursiveCuts(n)
# print(cuts)
minimum_cuts = unitCut(n)
print('value', min_time_to_cut(50000))
print(f"Minimum number of cuts: {minimum_cuts}")




    



