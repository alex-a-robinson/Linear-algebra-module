
def matrixCorrectlyFormed(data):
	if type(data) is not list:
		return False
	if len(data) > 0:
		rowLength = len(data[0])
		for row in data:
			if type(row) is not list:
				return False
			if len(row) != rowLength:
				return False
			for item in row:
				if not isinstance(item, (int, float, complex)):
					return False
	return True
	
def zeros(s):
	a = []
	numRows = s[0]
	numCols = s[1]
	for r in range(numRows):
		a.append([])
		for c in range(numCols):
			a[r].append(0)
	return matrix(a)
			
def dot(a, b):
	if isinstance(a, matrix) and isinstance(b, matrix) and a.numCols == b.numRows:
		result = zeros((a.numRows, b.numCols))
		for r, row in enumerate(a.rows):
			for c, col in enumerate(b.cols):
				result[r][c] = sum([a*b for a,b in zip(row, col)])
		return result
		
	else:
		raise Exception((a, b), "Matrix type expected")
	
class matrix():
	
	def __init__(self, data):
		if matrixCorrectlyFormed(data):
			self.amatrix = data
		else:
			raise Exception(data, "Matrix not correctly formed")
	
	def __str__(self):
		prettyMatrix = []
		for row in self.amatrix:
			prettyMatrix.append("[" + ", ".join([str(n) for n in row]) + "],")
		return "[" + "\n".join(prettyMatrix)[:-1] + "]"
	

	def __len__(self):
		size = 0
		for row in self.amatrix:
			size += len(row)
		return size
			
	def __iter__(self):
		for row in self.amatrix:
			for item in row:
				yield item
	
	def __getitem__(self, key):
		return self.amatrix[key]
	
	def __setitem__(self, key, value):
		if type(value) is list:
			if len(value) == self.numCols:
				self.amatrix[key] = value
			else:
				raise Exception(value, "New value must have same number of columns as matrix")
		else:
			raise Exception(value, "Value must be of type list")	
	
	@property
	def numRows(self):
		return len(self.amatrix)
		
	@property
	def numColumns(self):
		return len(self.amatrix[0]) # All rows have same # of elements so use first
	
	numCols = numColumns
	
	@property
	def size(self):
		return (self.numRows, self.numCols)
	
	def row(self, n):
		if n > self.numRows:
			raise Exception(n, "Index is out of range of matrix")
			return []
		return self.amatrix[n]
	
	def column(self, n):
		if n > self.numCols:
			raise Exception(n, "Index is out of range of matrix")
			return []
		col = []
		for row in self.amatrix:
			col.append(row[n])
		return col
		
	col = column
	
	def col(self, n):
		return self.column(n)
	
	@property
	def rows(self):
		a = []
		for i in range(self.numRows):
			a.append(self.row(i))
		return a
	
	@property
	def columns(self):
		a = []
		for i in range(self.numCols):
			a.append(self.col(i))
		return a
	
	cols = columns 
	
	@property
	def sum(self):
		s = 0
		for row in self.amatrix:
			for item in row:
				s += item
		return s
		
	def item(self, i):
		row = i[0]
		col = i[1]
		return self.amatrix[row][col]			
		
	def edit(self, i, n):
		row = i[0]
		col = i[1]
		self.amatrix[row][col] = n
	
	def __add__(self, other):
		result = zeros(self.size)
		if isinstance(other, (int, float, complex)):
			for rowIndex in range(self.numRows):
				for colIndex in range(self.numCols):
					a = self[rowIndex][colIndex]
					result[rowIndex][colIndex] = a + other
					
		elif isinstance(other, matrix):
			for rowIndex in range(self.numRows):
				for colIndex in range(self.numCols):
					a = self[rowIndex][colIndex]
					b = other[rowIndex][colIndex]
					result[rowIndex][colIndex] = a + b
		
		else:
			raise Exception(other, "Must be of type matrix or int,float,complex")			
					
		return result
	
	def __radd__(self, other):
		return self.__add__(other)
		
	def __sub__(self, other):
		result = zeros(self.size)
		if isinstance(other, (int, float, complex)):
			for rowIndex in range(self.numRows):
				for colIndex in range(self.numCols):
					a = self[rowIndex][colIndex]
					result[rowIndex][colIndex] = a - other

		elif isinstance(other, matrix):
			for rowIndex in range(self.numRows):
				for colIndex in range(self.numCols):
					a = self[rowIndex][colIndex]
					b = other[rowIndex][colIndex]
					result[rowIndex][colIndex] = a - b

		else:
			raise Exception(other, "Must be of type matrix or int,float,complex")			

		return result
	
	def __rsub__(self, other): # TODO: Order matters this will not work
		return self.__sub__(other)
		
	def __mul__(self, other):
		result = zeros(self.size)
		if isinstance(other, (int, float, complex)):
			for rowIndex in range(self.numRows):
				for colIndex in range(self.numCols):
					a = self[rowIndex][colIndex]
					result[rowIndex][colIndex] = a * other
					
		elif isinstance(other, matrix):
			for rowIndex in range(self.numRows):
				for colIndex in range(self.numCols):
					a = self[rowIndex][colIndex]
					b = other[rowIndex][colIndex]
					result[rowIndex][colIndex] = a * b
		
		else:
			raise Exception(other, "Must be of type matrix or int,float,complex")			
					
		return result 
	
	def __rmul__(self, other):
		return self.__mul__(other)
		
	def __truediv__(self, other):
		result = zeros(self.size)
		if isinstance(other, (int, float, complex)):
			for rowIndex in range(self.numRows):
				for colIndex in range(self.numCols):
					a = self[rowIndex][colIndex]
					result[rowIndex][colIndex] = a / other

		elif isinstance(other, matrix):
			for rowIndex in range(self.numRows):
				for colIndex in range(self.numCols):
					a = self[rowIndex][colIndex]
					b = other[rowIndex][colIndex]
					result[rowIndex][colIndex] = a / b

		else:
			raise Exception(other, "Must be of type matrix or int,float,complex")			

		return result 
	
	def __rturediv__(self, other): #TODO this will not work as order matter
		return self.__div__(other)

		
	
	def flaten(self):
		a = []
		for i in self:
			a.append(i)
		return a
	
	def tolist(self):
		return self.amatrix
		
	def reshape(self, size):
		a = self.flaten()
		rows = []
		result = []
		if sum(self.size) == sum(size):
			for r in range(size[0]):
				row = []
				for c in range(size[1]):
					row.append(a[r * size[1] + c])
				rows.append(row)
			return matrix(rows)
		else:
			raise(Exception(size, "Matrix size must be the same number of items"))
	
		
				
a = matrix([[1, 2, 3],
 			[4, 5, 6]])
b = matrix([[7, 8],
 			[9, 10],
			[11, 12]])

print(dot(a, b))
print(a.reshape((3,2)))
