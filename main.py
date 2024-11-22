
import random

mydict = [
    "rock",
    "paper",
    "scissors"
]

def getChoices():
    playerChoice = input("Choose A Random Selection (Rock, Paper, Scissors) ")
    botChoice = random.choice(mydict)

    if playerChoice == "rock" and botChoice == "scissors":
        print("You Won!")
        print(f"Bot Picked {botChoice}")
        print(f"You Picked {playerChoice}")
    elif playerChoice == "rock" and botChoice == "rock":
        print("Draw!")
        print(f"Bot Picked {botChoice}")
        print(f"You Picked {playerChoice}")
    elif playerChoice == "rock" and botChoice == "paper":
        print("Bot Won")
        print(f"Bot Picked {botChoice}")
        print(f"You Picked {playerChoice}")  
    elif playerChoice == "paper" and botChoice == "rock":
        print("You Won!")
        print(f"Bot Picked {botChoice}")
        print(f"You Picked {playerChoice}") 
    elif playerChoice == "paper" and botChoice == "paper":
        print("Draw!")
        print(f"Bot Picked {botChoice}")
        print(f"You Picked {playerChoice}") 
    elif playerChoice == "paper" and botChoice == "scissors":
        print("Bot Wins!")
        print(f"Bot Picked {botChoice}")
        print(f"You Picked {playerChoice}") 
    elif playerChoice == "scissors" and botChoice == "scissors":
        print("Draw")
        print(f"Bot Picked {botChoice}")
        print(f"You Picked {playerChoice}") 
    elif playerChoice == "scissors" and botChoice == "rock":
        print("Bot Won!")
        print(f"Bot Picked {botChoice}")
        print(f"You Picked {playerChoice}") 
    elif playerChoice == "scissors" and botChoice == "paper":
        print("You Won!") 
        print(f"Bot Picked {botChoice}")
        print(f"You Picked {playerChoice}")  

    getChoices() 

getChoices() 


#\\\\----------------Project 3---------------------////#
