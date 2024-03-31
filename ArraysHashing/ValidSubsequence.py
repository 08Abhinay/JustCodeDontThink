def isValidSubsequence(array, sequence):
    prev_index = -1  

    for num in sequence:
        # Check if num is in the remaining part of array (after prev_index)
        if num in array[prev_index + 1:]:
            # Update prev_index to the index of the found num, relative to the entire array
            prev_index = array.index(num, prev_index + 1)
        else:
            return False
    return True
