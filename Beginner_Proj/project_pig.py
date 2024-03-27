''' Here you are rolling a dice
-> You have the roll the dice till you got 1
-> you keep on adding the number which are greather than 1
-> If you got '1' while rolling a dice done, it the end you chance is done
-> Count the toatl number you got in your chance
'''
import random

#random dice number
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

#value =roll()
#print(value)

#players

while True:
    players = input("Enter the number od players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print("Must be between (2-4)")
    else:
        print("Inavlid Inpur, try again")
#print(players)

#scores

max_score = 50
players_scores =[0 for _ in range(players)]
#print(players_scores)

while max(players_scores) < max_score:
    
    for player_id in range(players):
        print("\n Player number", player_id+1, "turn has just started!")
        print("Your total score is: ", players_scores[player_id],"\n")
        current_score=0
        
        while True:
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower() != 'y':
                break
            
            value=roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score=0
                break
            else:
                current_score += value
                print(f"you rolled a:{value}")

            print(f"Your current score is:{current_score}")

        players_scores[player_id] += current_score
        print("Total score is: ",players_scores[player_id])

max_score = max(players_scores)
winning_id = players_scores.index(max_score)
print(f"player number:{winning_id +1}, is the winner with the max score of: {max_score}")