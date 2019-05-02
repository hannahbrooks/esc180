def rule (val, mylist):
	mysum = 0
	
	for i in mylist:
		mysum+= i

	if val == 1:
		if mysum == 2 or mysum == 3:
			return 1
		else:
			return 0
	else:
		if mysum == 3:
			return 1
		else:
			return 0
