for i in range(1, 6):
	if i % 2 != 0:
		for j in range(1, 6):
			print(j, end=' ')
	else:
		for j in range(1, 6):
			print("0", end=' ')
	print()