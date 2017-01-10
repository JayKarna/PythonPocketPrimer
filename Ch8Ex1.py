"""
Create a set of custom Python classes that model the relationships that exist among the following 2D shapes: quadrilateral, parallelogram, rectangle, 
rhombus, and square
"""
class quadrilateral:
	def func(self):
		print('This is a quadrilateral')

class parallelogram(quadrilateral):
	def func(self):
		print('This is a parallelogram')
		super().func()

class rectangle(parallelogram):
	def func(self):
		print('This is a rectangle')
		super().func()

class rhombus(parallelogram):
	def func(self):
		print('This is a rhombus')
		super().func()

class square(rectangle, rhombus):
	def func(self):
		print('This is a square')
		super().func()

if __name__ == '__main__':
	shapeA = quadrilateral()
	shapeA.func()
	print()

	shapeB = parallelogram()
	shapeB.func()
	print()

	shapeC = rectangle()
	shapeC.func()
	print()

	shapeD = rhombus()
	shapeD.func()
	print()

	shapeE = square()
	shapeE.func()

	