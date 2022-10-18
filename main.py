import random
from game_data import data
from higherlower_art import vs, logo

import os
clear = lambda: os.system('cls')


def select_profile():
	num = random.randint(0,len(data)-1)
	return data[num]
	
def compare_profiles(a, b):
	if a["follower_count"] > b["follower_count"]:
		return a
	else:
		return b
		
def print_profile(a):

	name = a["name"]
	profesh = a["description"]
	country = a["country"]
	followers = a["follower_count"]
	
	return(f"{name}, a {profesh}, from {country}.")

def play_game():
	
	clear()
	vs_a = select_profile()
	vs_b = select_profile()
	
	while vs_a == vs_b:
		vs_b = select_profile()

	game_active = True
	score = 0
	print(logo)
	
	while game_active == True:
		
		if score > 0:
			clear()
			print(logo)
			print(f"Correct, your score is: {score}")
		
		
		print("Compare A:",print_profile(vs_a))
		print(vs)
		print("Compare B:",print_profile(vs_b))
		
		if input("Who has more followers? a or b?") == "a":
			if vs_a == compare_profiles(vs_a, vs_b):
				score += 1
				vs_b = select_profile()
			else:
				print(f"Wrong. Your score is {score}")
				game_active = False
				if input("Play again? (y/n)") == "y": play_game()
				
		else:
			if vs_b == compare_profiles(vs_a, vs_b):
				score += 1
				vs_a = vs_b
				vs_b = select_profile()
			else:
				print(f"Wrong. Your score is {score}")
				game_active = False	
				if input("Play again? (y/n)") == "y": play_game()
		
play_game()
