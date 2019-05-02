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
                else:
                     for i in range (0, r, 1):
                                l = []
                                for i in range (0, c, 1):
                                        l+= [0]
                                self.matrix+= [l] 

                print(self.matrix)  

        def setPos(self, row, col, val):
                self.matrix[row-1][col-1] = val
                return True

        def getNeighbours(self, row, col):
                l = []
                lengthr = len(self.matrix)
                lengthc = len(self.matrix[0])
                l+= [self.matrix[(row-1) % lengthr][(col-1) % lengthc]]
                l+= [self.matrix[(row-1) % lengthr][col % lengthc]]
                l+= [self.matrix[(row-1) % lengthr][(col+1) % lengthc]]
                l+= [self.matrix[row % lengthr][(col-1) % lengthc]]
                l+= [self.matrix[row % lengthr][(col+1) % lengthc]]
                l+= [self.matrix[(row+1) % lengthr][(col-1) % lengthc]]
                l+= [self.matrix[(row+1) % lengthr][col % lengthc]]
                l+= [self.matrix[(row+1) % lengthr][(col+1) % lengthc]]
                return l

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

        def evolve(self, myfunc):
                nextstate = []

                for i in range (0, len(self.matrix), 1):
                        l = []
                        for j in range (0, len(self.matrix[0]), 1):
                                l+= [0]
                        nextstate += [l]

                for i in range (0, len(self.matrix), 1):
                        for j in range (0, len(self.matrix[0]), 1):
                                nextstate[i][j] = myfunc(self.matrix[i][j], self.getNeighbours(i, j))

                self.matrix = nextstate
