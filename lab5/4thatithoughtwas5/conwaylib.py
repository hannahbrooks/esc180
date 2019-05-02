import random

class conway:
	def __init__ (self, r, c, s):
		self.matrix = []

		if s == "random":
			for i in range (0, r, 1):
				l = []
				for i in range (0, c, 1):
					x = random.randint(0,1)
					l+= [x]
				self.matrix+= [l]

	def setPos(self, row, col, val):
		self.matrix[row][col] = val
		return True

	def getNeighbours(self, row, col):
		l = []
		lengthr = len(self.matrix)
		lengthc = len(self.matrix[0])
		l+= [self.matrix[row-1][col]]
		l+= [self.matrix[row+(lengthr % (lengthr-row+1))][col]]
		l+= [self.matrix[row][col-1]]
		l+= [self.matrix[row][col+(lengthc % (lengthc-col-1))]]
		l+= [self.matrix[row+(lengthr % (lengthr-row+1))][col+(lengthc % (lengthc-col-1))]]
		l+= [self.matrix[row+(lengthr % (lengthr-row+1))][col-1]]
		l+= [self.matrix[row-1][col+(lengthc % (lengthc-col-1))]]
		l+= [self.matrix[row+(lengthr % (lengthr-row+1))][col-1]]
		print(str(l))
		return True

	def printDisp(self):
		print(self.getDisp())
		return True

	def getDisp(self):
		mystr = ""
		for i in self.matrix:
			mystr+="\n"
			for j in i:
				if j == 0:
					mystr+= " "
				elif j == 1:
					mystr+= "*"
				else:
					mystr+= str(j)
		return mystr
