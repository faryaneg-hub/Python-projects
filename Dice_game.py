import random

name1 = input("Enter player-1 name: ")
name2 = input("Enter player-2 name: ")

turn = input("Who's turn to dice: ")

while True:
    user_input = input("\nEnd game: type'q'\nContinue game: press the 'Enter'\n")
    if user_input == 'q':
        break
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"{turn}: {dice1}, {dice2}")
    if turn == name1:
        turn = name2
    else:
        turn = name1
