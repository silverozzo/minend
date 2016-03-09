import random


class Cell():
	mined  = False
	opened = False
	neibs  = []
	point  = 0
	
	def __init__(self):
		self.mined  = False
		self.opened = False
		self.neibs  = []
		self.point  = 0
	
	def check_point(self):
		if self.mined:
			return
		
		for neib in self.neibs:
			if neib.mined:
				self.point += 1


class Field():
	cells = []
	
	def __init__(self, rows, cols, mines):
		self.cells = [[Cell() for x in range(cols)] for row in range(rows)]
		self.init_mines(mines)
		self.init_neibs()
	
	def init_mines(self, mines):
		counter = 0
		while counter < mines:
			row = random.randint(0, len(self.cells) - 1)
			col = random.randint(0, len(self.cells[0]) - 1)
			
			if self.cells[row][col].mined:
				continue
			
			self.cells[row][col].mined = True
			counter += 1
	
	def init_neibs(self):
		for row in range(len(self.cells)):
			for col in range(len(self.cells[row])):
				if row > 0 and col > 0:
					self.cells[row][col].neibs.append(self.cells[row - 1][col - 1])
				if row > 0:
					self.cells[row][col].neibs.append(self.cells[row - 1][col])
				if row > 0 and col < len(self.cells[row]) - 1:
					self.cells[row][col].neibs.append(self.cells[row - 1][col + 1])
				if col > 0:
					self.cells[row][col].neibs.append(self.cells[row][col - 1])
				if col < len(self.cells[row]) - 1:
					self.cells[row][col].neibs.append(self.cells[row][col + 1])
				if row < len(self.cells) - 1 and col > 0:
					self.cells[row][col].neibs.append(self.cells[row + 1][col - 1])
				if row < len(self.cells) - 1:
					self.cells[row][col].neibs.append(self.cells[row + 1][col])
				if row < len(self.cells) - 1 and col < len(self.cells[row]) - 1:
					self.cells[row][col].neibs.append(self.cells[row + 1][col + 1])
				self.cells[row][col].check_point()
	
	def get_state(self):
		state = [[cell.point for cell in row] for row in self.cells]
		return state
