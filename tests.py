import unittest

from field import Cell, Field


class TestCellModel(unittest.TestCase):
	def test_simple_creation(self):
		cell = Cell(0, 0)
		self.assertEqual(False, cell.opened)
		self.assertEqual(False, cell.mined)
		self.assertEqual(False, cell.marked)


class TestFieldModel(unittest.TestCase):
	def test_simple_init(self):
		field = Field(3, 3, 0)
		self.assertEqual(False, field.finished)
		self.assertEqual(False, field.loosed)
		self.assertEqual(0,     field.rest)
		
		field.open(0, 0)
		self.assertEqual(True,  field.finished)
		self.assertEqual(False, field.loosed)
	
	def test_get_line_for_next(self):
		field = Field(3, 3, 0)
		field.cells[-1][0].mined = True
		field.cells[-1][1].mined = True
		
		line = field.get_line_for_next()
		self.assertEqual(True,  line[0])
		self.assertEqual(True,  line[1])
		self.assertEqual(False, line[2])
	
	def test_init_with_line(self):
		pass


if __name__ == '__main__':
	unittest.main()
