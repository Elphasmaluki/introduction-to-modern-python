import math

def is_perfect_square(n):
	square_root = int(math.sqrt(n))
	return square_root * square_root == n

num = int(input("Enter a number: "))
value1 = 5 * (num * num) + 4
value2 = 5 * (num * num) - 4

def check_fibonacci():
	if is_perfect_square(value1) or is_perfect_square(value2):
		print(f"{num} is a Fibonacci number.")
	else:
		print(f"{num} is not a Fibonacci number.")
check_fibonacci()