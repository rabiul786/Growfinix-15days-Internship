# Task 1 - Number guessing game
import random


def play_game():
    number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("I am thinking of a number between 1 and 100.")
    print("You have", max_attempts, "attempts.")

    while attempts < max_attempts:
        guess = input("Your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! You got it in", attempts, "attempts.")
            return

    print("Game over. The number was", number)


def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ")
        if again.lower() != "y":
            print("Thanks for playing!")
            break


main()
