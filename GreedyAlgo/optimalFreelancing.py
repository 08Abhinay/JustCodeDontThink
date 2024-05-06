def optimalFreelancing(jobs):
    # Write your code here.

    total_days = 7
    profit = 0
    jobs.sort(key=lambda x: x['payment'], reverse= True)
    # print(jobs)
    schedule = [False] * total_days
    
    for job in jobs:
        maxtime = min(job['deadline'], total_days)
        for time in reversed(range(maxtime)):
            if schedule[time] == False:
                schedule[time] = True
                profit += job['payment']
                break
        

    return profit