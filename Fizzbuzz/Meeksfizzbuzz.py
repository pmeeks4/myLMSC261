count = 0
while(count < 100):
	count = count + 1
	if count % 3 == 0 and count % 5 == 0:
		print("fizzbuzz")
	elif count % 3 == 0:
		print("fizz")
	elif count % 5 == 0:
		print("buzz")
	else:
		print(count)
