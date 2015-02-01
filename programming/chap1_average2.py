#!/usr/bin/env python3

numbers = []
total = 0
lowest = None
highest = None
count = None
median = None

while True:
	try:
		line = input("enter a number or Enter to finish: ")
		if not line:
			break
		number = int(line)
		numbers.append(number)
		total += number
		if lowest is None or lowest > number:
			lowest = number
		if highest is None or highest < number:
			highest = number
	except ValueError as err:
		print(err)

count = len(numbers)
print("numbers:", numbers)

numbers.sort()

if count:
	if count % 2 == 0:
		median = (numbers[int(count/2) - 1] + numbers[int(count/2)]) / 2
	else:
		median = numbers[int(count/2)]

	print("count =", count,
			"sum =", total,
			"lowest =", lowest,
			"highest =", highest,
			"median =", median,
			"mean =", total/count)
