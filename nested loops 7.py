no_of_elements = 0
rows = 4
subpyramid_start = rows + 1
for i in range(0, rows):
	no_of_elements +=1
	for j in range(rows - no_of_elements, 0, -1):
		print(" ", end='')
	print(i + 1, end=" ")
	for k in range(subpyramid_start, subpyramid_start + (no_of_elements - 1)):
		print(k, end=' ')
	print()
	subpyramid_start += (no_of_elements - 1)