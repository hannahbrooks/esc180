def bubbleSort(A):
	mylist = A
	n = len(mylist)
	swapped = True
	temp = 0

	for i in mylist:
		if i == None:
			return [False], [mylist]

	while swapped == True:
		swapped = False
		for i in range(1, n, 1):
			if mylist[i-1] > mylist[i]:
				temp = mylist[i-1]
				mylist[i-1] = mylist[i]
				mylist[i] = temp
				swapped = True
	return [True], [mylist]


