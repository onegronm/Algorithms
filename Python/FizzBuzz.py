
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops BEFORE a specified number.
for i in range(1, 101):
	if i%3 == 0 and i%5 == 0:
		print("FizzBuzz")
	elif i%3 == 0:
		print("Fizz")
	elif i%5 == 0:
		print("Buzz")
	else:
		print(i)
	
