import random

print("lets play hangman uwu ")

words = ["high school musical two","peppa pig","endgame","gay rights","sunmi can step on me"]
word = random.choice(words)



while True:
	diff = input("which difficulty would you like ? hard = 5 guesses, med = 10 guesses, easy = 15 guesses, or press 'q' to exit :) ")

	hard = 5
	med = 10
	easy = 15

	if diff == "hard":
		letter = input("pick a letter, friend~ ")
		if letter in word:
			print("correct ! :)")
		else:
			print("miss ;(")
			hard -=1
		print("guesses remaining: " + str(hard))

	elif diff == "med":
		letter = input("pick a letter, friend~")
		if letter in word:
			print("correct ! :)")
		else:
			print("miss ;(")
			med -=1
		print("guesses remaining: " + str(med))


	elif diff == "easy":
		letter = input("pick a letter, friend~")
		if letter in word:
			print("correct ! :)")
		else:
			print("miss ;(")
			easy -=1
		print("guesses remaining: " + str(easy))

	elif diff=="q":
		break

	else:
		print("wait choose again i dont understand :(")

