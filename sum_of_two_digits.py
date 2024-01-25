def sum_two_digits(digits):
	lst = digits.split()	
	return int(lst[0]) + int(lst[1])

digitis = input()

print(sum_two_digits(digitis))
