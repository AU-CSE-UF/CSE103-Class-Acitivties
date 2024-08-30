no_of_elements = 0
start_element = 1
rows = 4
for i in range(0, rows):
	no_of_elements +=1
	for j in range(rows - no_of_elements, 0, -1):
		print(" ", end='')
	for j in range(start_element, start_element + no_of_elements):
		print(j, end=' ')
	print()
	start_element += no_of_elements