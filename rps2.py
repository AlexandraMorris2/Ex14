def instructions():
	print("You have not entered a recognised character")
	print("Instructions to play Rock Paper Scissors")
	print("Press r for rock or p for paper or s for scissors and then enter")

def welcome():
	print("let's play a game of rock, paper, scissors")
	print("r= rock, p= paper, s= scissors")
	print("rock smashes scissors, paper wraps rock, scissors cut paper")
	print("Good Luck")


welcome()
user_input = input("please choose your move:")
for _ in user_input:
	if user_input == "r":
		print("you chose: rock")

	elif user_input == "p":
		print("you chose: paper")

	elif user_input == "s":
		print("you chose: scissors")


from random import randint


for _ in range(1):
	value = randint(0, 2)
#if value != range:
	#print("wrong")

	if value == 0:
		print("computer chose: rock")

	elif value == 1:
		print("computer chose: paper")

	elif value == 2:
		print("computer chose: scissors")


	if user_input == "r" and value == 0:
		print("you both chose rock, its a tie")

	elif user_input == "p" and value == 1:
		print("you both chose paper, its a tie")

	elif user_input == "s" and value == 2:
		print("you both chose scissors, its a tie")

	elif user_input == "r" and value == 1:
		print("paper covers rock, you lose")

	elif user_input == "s" and value == 1:
		print("scissors cut paper, you win!")

	elif user_input == "r" and value == 2:
		print("rock smashes scissors, you win!")

	elif user_input == "p" and value == 2:
		print("scissors cut paper, you lose")

	elif user_input == "p" and value == 0:
		print("paper wraps rock, you win!")

	elif user_input == "s" and value == 0:
		print("rock smashes scissors, you lose")

	else:
		print(instructions())
		try_again = (input("would you like to try again? y/n"))
		if "n" in try_again:
			print("ok goodbye :)")


	#need to add the no option to run the code again
	#why is it printing none?
	#how can i change the code to include functions