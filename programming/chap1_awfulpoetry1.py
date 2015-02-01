#!/usr/bin/env python3

import random

articles = ["the", "a"]
subjects = ["cat", "dot", "man", "woman"]
verbs = ["jump", "lough", "run"]
adverbs = ["loudly", "quietly", "well", "badly"]

for i in range(0,5):
	article = random.choice(articles)
	subject = random.choice(subjects)
	verb = random.choice(verbs)

	if random.randint(0, 1) == 0:
		print(i, ".", article, subject, verb)
	else:
		adverb = random.choice(adverbs)
		print(i, ".", article, subject, verb, adverb)
