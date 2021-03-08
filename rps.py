import random

# Printing the rules
print("""Winning Rules as follows :

Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.
	""")

while True:
	print("""The choices are:
			1. Rock
			2. Paper
			3. Scissor
		""")

	user_choice_number = int(input("Please choose: "))

	while user_choice_number > 3 or user_choice_number < 1:
		user_choice_number = int(input("Please choose again: "))

	if user_choice_number == 1:
		user_choice = "Rock"
	elif user_choice_number == 2:
		user_choice = "Paper"
	else:
		user_choice = "Scissor"

	print("You chose {}.".format(user_choice))

	computer_choice_number = random.randint(1, 3)

	while computer_choice_number == user_choice_number:
		computer_choice_number = random.randint(1, 3)

	if computer_choice_number == 1:
		computer_choice = "Rock"
	elif computer_choice_number == 2:
		computer_choice = "Paper"
	else:
		computer_choice = "Scissor" 

	print("Computer chose {}.".format(computer_choice))

	if ((user_choice_number == 1 and computer_choice_number == 2)
		or (user_choice_number == 2 and computer_choice_number == 1)):
		result = "paper"
	elif((user_choice_number == 1 and computer_choice_number == 3) 
		or (user_choice_number == 3 and computer_choice_number == 1)):
		result = "rock"
	else:
		result = "scissor"


	if result == user_choice:
		print("You win! You have {0} and the computer has {1}. {0} wins {1}."
			. format(user_choice, computer_choice))
	else:
		print("You lose! You have {0} and the computer has {1}. {0} wins {1}"
			.format(user_choice, computer_choice))


	ans = input("Do you want to play again? ")

	if ans == "no" or ans == "n":
		break

