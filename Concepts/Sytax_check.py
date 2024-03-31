def tournamentWinner(competitions, results):
    # Write your code here.
    # Initialize a dictionary to keep track of scores
    scores = {}
    # Maximum score and current best team
    
    for (team1, team2), result in zip(competitions, results):

        winning_team = team1 if result == 1 else team2
        
        if winning_team in scores:
            scores[winning_team] += 3
        else:
            scores[winning_team] = 3

    return max(scores, key=scores.get)
        
        

competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]

print(tournamentWinner(competitions,results))