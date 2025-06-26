import random

print("====================================")
print("Rock, Paper, Scissors, Lizard, Spock")
print("====================================")


print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")

options = ["✊", "✋", "✌️", "🦎", "🖖"]
player = int(input("Pick a number!: "))
computer = random.randint(1,5)


    
print(f"You Choose: {options[player-1]}")
print(f"CPU Choose: {options[computer-1]}")

#Results#
if player == 1 and computer ==2:
    print("You Lose!")
elif player == 1 and computer ==5:
    print("You Lose!")
elif player == 1 and computer ==3:
    print("You Win!")
elif player == 1 and computer ==4:
    print("You Win!")
if player == 2 and computer == 1:
    print("You Win!")
elif player == 2 and computer ==5:
    print("You Win!")
elif player == 2 and computer ==4:
    print("You Lose!")
elif player == 2 and computer ==3:
    print("You Lose!")
elif player == 3 and computer == 5:
    print("You lose!")
elif player == 3 and computer == 1:
    print("you lose!")
elif player == 3 and computer == 2:
    print("You Win!")
elif player == 3 and computer == 4:
    print("You Win!")
elif player == 4 and computer == 1:
    print("You Lose!")
elif player == 4 and computer == 3:
    print("You Lose!")
elif player == 4 and computer == 5:
    print("You Win!")
elif player == 4 and computer == 2:
    print("You Win!")
elif player == 5 and computer == 2:
    print("You Lose!")
elif player == 5 and computer == 4:
    print("You Lose!")
elif player == 5 and computer == 1:
    print("You Win!")
elif player == 5 and computer == 3:
    print("You Win! ")
else:
    print("Draw!")