def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    total_time = 0
    sum = 0 
    for i in range(len(queries)):

        if any(queries[:i]):
            sum = sum + queries[i-1]
        else:
            sum = 0
        total_time += sum
        
    return total_time


queries = [3, 2, 1, 2, 6]
print(minimumWaitingTime(queries))


#Solution 2

def minimumWaitingTime(queries):
    # Write your code here.

    total_min_time = 0
    queries.sort()
    for idx, query in enumerate(queries):

        queries_left = len(queries) - (idx + 1)
        # print(len(queries), idx)
        total_min_time += queries_left * query
        
    
    return total_min_time
