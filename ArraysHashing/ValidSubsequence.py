def isValidSubsequence_solution1(array, sequence):
    prev_index = -1  

    for num in sequence:
        # Check if num is in the remaining part of array (after prev_index)
        if num in array[prev_index + 1:]:
            # Update prev_index to the index of the found num, relative to the entire array
            prev_index = array.index(num, prev_index + 1)
        else:
            return False
    return True


def isValidSubsequence_solution2(array, sequence):
    
    arrIdx = 0 
    seqIdx = 0 

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


def isValidSubsequence_solution3(array, sequence):
    # Write your code here.
    seqIdx = 0 

    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1

    return seqIdx == len(sequence)
