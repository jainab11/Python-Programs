# Gambler
# a. Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
# he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
# times he/she wins and the number of bets he/she makes. Run the experiment N
# times, averages the results, and prints them out.
# b. I/P -> $Stake, $Goal and Number of times
# c. Logic -> Play till the gambler is broke or has won
# d. O/P -> Print Number of Wins and Percentage of Win and Loss
import random

def gamble(stake, goal):
    bets = 0
    wins = 0
    
    while stake > 0 and stake < goal:
        bets += 1
        if random.choice([True, False]):
            stake += 1
            wins += 1
        else:
            stake -= 1
    
    return wins, bets

def simulate_gambler(stake, goal, times):
    total_wins = 0
    total_bets = 0
    
    for _ in range(times):
        wins, bets = gamble(stake, goal)
        total_bets += bets
        total_wins += wins
    
    return total_wins, total_bets

def main():
    stake = int(input("Enter the starting stake: "))
    goal = int(input("Enter the goal: "))
    times = int(input("Enter the number of times to run the experiment: "))
    
    total_wins, total_bets = simulate_gambler(stake, goal, times)
    
    print("Number of Wins:", total_wins)
    print("Number of Bets:", total_bets)
    print("Percentage of Win:", (total_wins / times) * 100, "%")
    print("Percentage of Loss:", ((total_bets - total_wins) / times) * 100, "%")

if __name__ == "__main__":
    main()
