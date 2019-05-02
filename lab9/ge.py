def ge_fw(matrix):
	mymatrix = matrix
	rows = len(mymatrix)
	columns = len(mymatrix[0])

	currentrow = 0
	currentcol = 0

	while (currentcol < columns):
		for i in range(currentrow,rows, 1):
			if mymatrix[i][currentcol] != 0:
				temp = []
				temp = mymatrix[currentrow]
				mymatrix[currentrow] = mymatrix[i]
				mymatrix[i] = temp
				break
		for hehe in range(0, 3, 1):
			print(str(mymatrix[hehe]))
		print("\n")
		for i in range(currentrow+1, rows, 1):
			if mymatrix[i][currentcol] != 0:
				c = mymatrix[i][currentcol] / mymatrix[currentrow][currentcol]
				for j in range(0, columns, 1):
					mymatrix[i][j]  = mymatrix[i][j] - c*int(mymatrix[currentrow][j])

		currentcol+=1
		currentrow+=1
		for hehe in range(0, 3, 1):
			print(str(mymatrix[hehe]))
		print("\n")
	return mymatrix

def ge_bw(matrix):
	mymatrix = matrix
	rows = len(mymatrix)
	columns = len(mymatrix[0])

	currentrow = rows-1
	currentcol = columns-1

	while (currentcol > 0):
		for i in range(currentrow-1, -1, -1):
			if mymatrix[i][currentcol] != 0:
				c = mymatrix[i][currentcol] / mymatrix[currentrow][currentcol]
				for j in range(0, columns, 1):
					mymatrix[i][j] = mymatrix[i][j] - c*int(mymatrix[currentrow][j])
			for hehe in range(0, 3, 1):
				print(str(mymatrix[hehe]))
			print("\n")


		currentcol-=1
		currentrow-=1

	for i in range(len(mymatrix)):
		for j in range(len(mymatrix[0])):
			if (mymatrix[i][j] != 0):
				mymatrix[i][j] = mymatrix[i][j] / mymatrix[i][j]
		for hehe in range(0, 3, 1):
			print(str(mymatrix[hehe]))
		print("\n")

	return mymatrix

#ge_bw(ge_fw([[1,2,3], [0,2,4], [3,4,10]]))
