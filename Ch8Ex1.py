"""
Create a set of custom Python classes that model the relationships that exist among the following 2D shapes: quadrilateral, parallelogram, rectangle, 
rhombus, and square
"""
class quadrilateral:
	def __init__(self):
		print('This is a quadrilateral')

	def funcq(self):
		print('This is also a quadrilateral')

class parallelogram(quadrilateral):
	def __init__(self):
		print('This is a parallelogram')

	def funcp(self):
		print('This is also a parallelogram')

class rectangle(parallelogram):
	def __init__(self):
		print('This is a rectangle')

	def funcre(self):
		print('This is also a rectangle')

class rhombus(parallelogram):
	def __init__(self):
		print('This is a rhombus')

	def funcrh(self):
		print('This is also a rhombus')

class square(rectangle, rhombus):
	def __init__(self):
		print('This is a square')

if __name__ == '__main__':
	shapeA = quadrilateral()

	shapeB = parallelogram()
	shapeB.funcq()

	shapeC = rectangle()
	shapeC.funq()
	shapeC.funcp()

	shapeD = rhombus()
	shapeD.funq()
	shapeD.funcp()

	shapeE = square()
	shapeE.funcq()
	shapeE.funcp()
	shapeE.funcre()
	shapeE.funcrh()

	