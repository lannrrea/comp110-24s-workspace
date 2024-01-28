"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730241802"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

secret_location: int = int(input("Pick a secret boat location between 1 and 4: "))
if secret_location > 4:
    print(f"Error! {secret_location} too high!")
    exit()
if secret_location < 1:
    print(f"Error! {secret_location} too low!")
    exit()

player2_guess: int = int(input("Guess a number between 1 and 4: "))
if player2_guess > 4:
    print(f"Error! {player2_guess} too high!")
    exit()
if player2_guess < 1:
    print(f"Error! {player2_guess} too low!")
    exit()

if secret_location == player2_guess == 1:
    print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    print("Correct! You hit the ship.")
if secret_location == player2_guess == 2:
    print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
    print("Correct! You hit the ship.")
if secret_location == player2_guess == 3:
    print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
    print("Correct! You hit the ship.")
if secret_location == player2_guess == 4:
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
    print("Correct! You hit the ship.")

if secret_location != player2_guess:
    if player2_guess == 1:
        print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship.")
    if player2_guess == 2:
        print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship.")
    if player2_guess == 3:
        print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship.")
    if player2_guess == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)
        print("Incorrect! You missed the ship.")
