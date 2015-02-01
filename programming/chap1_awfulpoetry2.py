#!/usr/bin/env python3

import random

articles = ["the", "a"]
subjects = ["cat", "dot", "man", "woman"]
verbs = ["jump", "lough", "run"]
adverbs = ["loudly", "quietly", "well", "badly"]
value = None

try:
	value = int(input("Enter a random number between 1 to 10:"))

	if value is None:
		value = 5

	if 1 <= value <= 10:
		for i in range(0, value):
			article = random.choice(articles)
			subject = random.choice(subjects)
			verb = random.choice(verbs)

			if random.randint(0, 1) == 0:
				print(i, ".", article, subject, verb)
			else:
				adverb = random.choice(adverbs)
				print(i, ".", article, subject, verb, adverb)
	else:
		print("Invalid number:", value)
		
except ValueError:
	print("Oops! Invalid input!")
