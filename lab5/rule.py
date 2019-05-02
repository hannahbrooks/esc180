def rule (val, mylist):
	sum = 0
	for i in range (0, len(mylist), 1):
		sum+= i
	if val == 1:
		if sum == 2 or sum == 3:
			return 1
		else:
			return 0
	else:
		if sum == 3:
			return 1
		else:
			return 0
