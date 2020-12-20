#This rock, paper, scissors game is for a computer and human.
 
#import random module for the computer's guess
import random 

#create a list of valid inputs
options = ["rock","paper","scissors"]
"rock" > "paper" > "scissors"

#generate a random guess from the computer
computerChoice = options[random.randint(0,2)]
#ask the human for their name
humanPlay = input("What is your name? ")
#ask the human if they want to play
want_to_play = input("Do you want to play? (Yes or NO)")
#if the human's response is yes, then play. Otherwise, end the game.
if want_to_play == 'yes':

#get input from the human
    human_play = input("Enter 'Rock, paper or scissors' ").lower()
    print("Hal's play: ",computerChoice)
#compare the answers and declare a winner
    if humanPlay > computerChoice:
        print("You win, ", human)
    elif computerChoice > humanPlay:
        print("You win, Hal!")
    else:
        print("It's a tie!")

#if the answer is no, end the game

if want_to_play == "no":
    print("Goodbye!")



