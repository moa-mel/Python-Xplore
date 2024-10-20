# Dictionary is used to store value in key:value pair
import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: ")
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice} # dictionary
    return choices

choices = get_choices()
print(choices)

# Dict = {1 : "Geeks", 2: "For", 3: "Geeks"}
