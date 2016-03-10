import random


class Cell():
	mined  = False
	opened = False
	neibs  = []
	point  = 0
	coords = ()
	
	def __init__(self, row, col):
		self.mined  = False
		self.opened = False
		self.neibs  = []
		self.point  = 0
		self.coords = (row, col)
	
	def check_point(self):
		if self.mined:
			self.point = 9
			return
		
		for neib in self.neibs:
			if neib.mined:
				self.point += 1
	
	def open(self, stack=[]):
		if self.opened:
			return stack
		
		if self.point > 0:
			self.opened = True
			print('open ' + str(self.coords))
			stack.append((self.coords, self.point))
			return stack
		
		if self.point == 0:
			self.opened = True
			stack.append((self.coords, self.point))
			for neib in self.neibs:
				print('neib ' + str(neib.coords))
				stack = neib.open(stack)
			return stack


class Field():
	cells = []
	
	def __init__(self, rows, cols, mines):
		self.cells = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
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
		state = [[cell.opened for cell in row] for row in self.cells]
		return state
	
	def open(self, row, col):
		stack  = self.cells[row][col].open()
		result = {}
		
		print('stack ' + str(stack))
		
		for item in stack:
			result[str(item[0][0]) + '-' + str(item[0][1])] = item[1]
		
		return result
