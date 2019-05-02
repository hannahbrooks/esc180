class seqdetector:
	def __init__(self):
		state = 0
		self.state=state

	def evolve (self,word):
		if word == "here":
			self.state = 1
		elif self.state == 1:
			if word == "are":
				self.state = 2
			else:
				self.state = 0
		elif self.state == 2:
			if word == "the":
				self.state = 3
			else:
				self.state = 0
		elif self.state == 3:
			if word == "solutions":
				self.state = 4
			else:
				self.state = 0
		elif self.state == 4:
			if word == "to":
				self.state = 5
			else:
				self.state = 0
		elif self.state == 5:
			if word == "the":
				self.state = 6
			else:
				self.state = 0
		elif self.state == 6:
			if word == "next":
				self.state = 7
			else:
				self.state = 0
		elif self.state == 7:
			if word == "exam":
				self.state = 8
			else:
				self.state = 0
		else:
			self.state = 0

		if self.state == 8:
			return True
		else:
			return False
