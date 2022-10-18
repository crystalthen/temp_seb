import random
from game_data import data
from higherlower_art import vs, logo

import os
clear = lambda: os.system('clear')


def select_profiles():
    a, b = random.sample(range(0,len(data)-1), 2)
    vs_profiles = {
        "a": data[a],
        "b": data[b]
    }
    return vs_profiles


def compare_profiles(a, b):
    if a["follower_count"] > b["follower_count"]:
        return a["name"]
    return b["name"]


def print_profile(profile):
    name = profile["name"]
    profesh = profile["description"]
    country = profile["country"]
    followers = profile["follower_count"]

    return(f"{name}, a {profesh}, from {country}.")


def play_game():
    score = 0
    while True:
        clear()
        print(logo)
        print(f"Your score is: {score}")

        vs_profiles = select_profiles()
        print("Compare A:",print_profile(vs_profiles["a"]))
        print(vs)
        print("Compare B:",print_profile(vs_profiles["b"]))

        # Ask for guess
        guess = input("Who has more followers? a or b? ")
        guess_name = vs_profiles[guess]['name']
        # Find the winner
        winner = compare_profiles(vs_profiles["a"], vs_profiles["b"])

        # Check if player guessed correctly
        if guess_name == winner:
            score += 1
            print(f"Correct, your score is: {score}")
            # Prompt to continue
            if input("Play again? (y/n) ") == "n":
                break
        else:
            print(f"Wrong. Your score is {score}")
            break


def main():
    play_game()


if __name__ == "__main__":
    main()
