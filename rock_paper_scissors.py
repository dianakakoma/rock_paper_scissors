#This rock, paper, scissors game is for a computer and human.
 
#import random module for the computer's guess
import random 

#create a list of valid inputs
options = ["rock","paper","scissors"]
"rock" > "paper" > "scissors"

#generate a random guess from the computer
computerChoice = options[random.randint(0,2)]

#ask the human for their name
name = input("What is your name? ")

#ask the human if they want to play
want_to_play = input("Do you want to play? (Yes or NO) ").lower()

#if the human's response is yes, then play. Otherwise, end the game.
if want_to_play == 'yes':
    print("okay")
    #get input from the human
    while True:
        choice = input("Enter 'rock, paper, scissors or stop'. ")
        #compare the answers and declare a winner or a tie
        if choice == "stop":
            print("Goodbye!")
            break

        elif choice > computerChoice:
            print(name, "wins!")
        elif computerChoice > choice:
            print("Hal won this round!")
        elif computerChoice == choice:
            print("It's a tie")
        else:
            print("Invalid response. Try again.")
            choice = input("Enter 'rock, paper, scissors or stop'. ")

#if the answer is no, end the game
else:
    print("Goodbye!")



