import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    players = input("Enter the number of players(max:4, min:2): ")
    if players.isdigit():
        players = int(players)
        if 2<= players<=4:
            break
        else:
            print("Must be between 2 and 4")

    else:
        print("Invalid,enter a integer next time")

max_score = 50
players_scores = [0 for _ in range(players)]
print(players_scores)

while max(players_scores)<max_score:
    for player_id in range(players):
        print("\nPlayer",player_id+1,"turn has just started" )
        print("Your current score is",players_scores[player_id],"\n")
        current_score =0

        while True:
            should_roll=input("Would you like to roll?(y/n) ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value ==1:
                print("You rolled 1! Turn done!")
                current_score = 0
                break
            else:
                current_score+=value
                print("you rolled:",value)

            print("Your score is ",current_score)
        players_scores[player_id]+=current_score
        print("Your total score is:",players_scores[player_id])

max_score = max(players_scores)
winning_id = players_scores.index(max_score)
print("Player number",winning_id+1,"is the winner with score",max_score)