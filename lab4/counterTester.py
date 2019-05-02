class counter:
	def __init__(self, initCnt):
		self.cnt=initCnt

	def evolve(self, x):
		self.cnt+=x
	def getState(self):
		return self.cnt

myCnt=counter(100)
alsoMyCnt=counter(1000)

myCnt.evolve(2)
myCnt.evolve(100)

alsoMyCnt.evolve(2)
alsoMyCnt.evolve(100)

print(myCnt.getState())
print(alsoMyCnt.getState())
