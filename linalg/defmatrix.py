def matrixCorrectlyFormed(data):
	"""
	Returns True if data is a valid input for matrix else False
	
	# Parameters
		data : list object
	
	# Returns
		Boolean
	"""
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

def dot(a, b):
	"""
	Returns the dot product of a and b
	
	# Parameters
		a,b : matrix objects
	
	# Returns
		A matrix objects representing a.b
	
	# Example
		>>> a = matrix([[1, 2],
		... 			[3, 4])
		>>> b = matrix([[5, 6],
		...		 	 	 7, 8])
		>>> dot(a, b)
		[[19, 22],
		 [43, 50]]
	"""
	if isinstance(a, matrix) or isinstance(b, matrix) or a.numCols != b.numRows:
		raise Exception((a, b), "Matrix type expected and a.numCols must equal b.numRows")
	
	result = zeros((a.numRows, b.numCols))
	for r, row in enumerate(a.rows):
		for c, col in enumerate(b.cols):
			result[r][c] = sum([a*b for a,b in zip(row, col)])
	return result

def shape(m, s):
	"""
	Returns a matrix reshaped to a certin size
	
	# Parameters
		m : matrix object
		s : tuple (number of rows, number of columns)
	
	# Returns
		A matrix object
	
	# Example
		>>> m = matrix([[1, 2],
		... 			[3, 4])
		>>> s = (4, 1)
		>>> shape(m, s)
		[[1],
		 [2],
		 [3],
		 [4]]
	"""
	if not isinstance(m, matrix):
		raise(TypeError(m, "Expected matrix type"))
	
	if sum(m.size) != sum(s):
		raise(Exception(s, "Both shapes must have the same number of elements"))
			
	f = flatten(m)
	rows = []
	for r in range(s[0]):
		row = []
		for c in range(s[1]):
			row.append(f[r * s[1] + c])
		rows.append(row)
	return matrix(rows)
		

def flatten(m):
	"""
	Returns a flattened matrix
	
	# Parameters
		m : matrix object
	
	# Returns:
		A list of items from the matrix
	
	# Example
		>>> m = matrix([[1, 2],
		... 			[3, 4])
		>>> flatten(m)
		[1, 2, 3, 4]
	"""
	a = []
	for i in m:
		a.append(i)
	return a

def ones(s):
	"""
	Returns a matrix of size s filled with ones
	
	# Parameters
		s : tuple (number of rows, number of columns)
			The size of the resulting matrix
	
	# Returns
		A matrix object of size s filled with 1s
	
	# See Also
		zeros()
		rand()
		randi()
	
	# Example
	>>> ones((2, 2))
	[[1, 1],
	 [1, 1]]
	"""
	a = []
	for r in range(s[0]):
		a.append([])
		for c in range(s[1]):
			a[r].append(1)
	return matrix(a) 
	
def zeros(s):
	"""
	Returns a matrix of size s filled with 0s
	
	# Parameters
		s : tuple (number of rows, number of columns)
			The size of the resulting matrix
	
	# Returns
		A matrix object of size s filled with 0s
	
	# See Also
		ones()
		rand()
		randi()
	
	# Example
	>>> zeros((2, 2))
	[[0, 0],
	 [0, 0]]
	"""
	a = []
	for r in range(s[0]):
		a.append([])
		for c in range(s[1]):
			a[r].append(0)
	return matrix(a)

def rand(s):
	"""
	Returns a matrix of size s filled with random numbers between 0 and 1
	
	# Parameters
		s : tuple (number of rows, number of columns)
			The size of the resulting matrix
	
	# Returns
		A matrix object of size s filled with random numbers between 0 and 1
	
	# See Also
		randi()
		zeros()
		ones()
	
	# Example
	>>> rand((2, 3))
	[[0.7781743846171062, 0.9439050707800642],
	 [0.2291032645819474, 0.24129115399154177],
	 [0.7946940974609309, 0.12921377900306463]]
	"""
	a = []
	for r in range(s[0]):
		a.append([])
		for c in range(s[1]):
			a[r].append(random.random())
	return matrix(a)
	
def randi(s, l, u):
	"""
	Returns a matrix of size s filled with random numbers between l and u
	
	# Parameters
		s : tuple (number of rows, number of columns)
			The size of the resulting matrix
		l : int
			The lower range of the random number
		u : int
			The upper range of the random number
	
	# Returns
		A matrix object of size s filled with random numbers between l and u
	
	# See Also
		zeros()
		ones()
		rand()
	
	# Example
	>>> randm((2, 2), 0, 10)
	[[3, 8],
	 [4, 1]]
	"""
	a = []
	for r in range(s[0]):
		a.append([])
		for c in range(s[1]):
			a[r].append(random.randint(l, u))
	return matrix(a)

def isSquareSize(s):
	"""
	Returns true if s represnets the size of a square matrix
	
	# Parameters
		s : tuple (number of rows, number of columns)
	
	# Returns
		Boolean : True if s represents the size of a square matrix
	
	# Example
	>>> s = (2, 3)
	>>> isSquareSize(s)
	False
	>>> s = (4, 4)
	>>> isSquareSize(s)
	True
	"""
	if s[0] == s[1]:
		return True
	else:
		return False

def identity(s):
	"""
	Returns the identity matrix of size s
	
	# Parameters
		s : tuple (number of rows, number of columns)
	
	# Returns
		a matrix object
	
	# Example
	>>> s = (2, 2)
	>>> identity(s)
	[[1, 0],
	 [0, 1]]
	"""
	if not isSquareSize(s):
		raise Exception(s, "Identiy matrix must be a square matrix")
	m = zeros(s)
	for i in range(s[0]):
		m[i][i] = 1
	return m
		

def inverse(m):
	pass

def detterminant(m):
	pass

def normalize(m):
	pass
	
def eigenvalues(m):
	pass

def eigenvectors(m):
	pass
	
def rot90(m):
	pass

def corss(m):
	pass

def kronecker_tensor_product(m):
	pass

class matrix():

	def __init__(self, data):
		if not matrixCorrectlyFormed(data):
			raise Exception(data, "Matrix not correctly formed")
		self.amatrix = data			
	
	def __str__(self):
		prettyMatrix = []
		for row in self.amatrix:
			prettyMatrix.append("[" + ", ".join([str(n) for n in row]) + "],")
		return "[" + "\n".join(prettyMatrix)[:-1] + "]"
	
	def __repr__(self):
		return str(self)

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
		if type(value) is not list:
			raise Exception(value, "Value must be of type list")
		
		if len(value) != self.numCols:
			raise Exception(value, "New value must have same number of columns as matrix")
		
		self.amatrix[key] = value
	
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
	
	def __rsub__(self, other): # ToDO; This will break if using scalers rather than matrix matrix
		return self.__sub__(other, self)
		
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
	
	def __rturediv__(self, other):
		return self.__div__(other, self)

	
	@property
	def numRows(self):
		"""
		Returns the number of rows in the matrix
		
		# Returns
			int
		
		# See Also
			self.numColumns()
			self.size()
			self.numCols()

		# Example
			>>> m = matrix([[1, 2],
			... 			[3, 4],
			... 			[5, 6]])
			>>> m.numRows
			3
		"""
		return len(self.amatrix)
		
	@property
	def numColumns(self):
		"""
		Returns the number of columns in the matrix
		
		# Returns
			int
		
		# See Also
			self.numRows()
			self.size()
			self.numCols()

		# Example
			>>> m = matrix([[1, 2],
			... 			[3, 4],
			... 			[5, 6]])
			>>> m.numColumns
			2
		"""
		return len(self.amatrix[0]) # All rows have same # of elements so use first
	
	numCols = numColumns
	
	@property
	def size(self):
		"""
		Returns a tuple containg the size of the matrix
		
		# Returns
			A tuple (number of rows, number of columns)
		
		# See Also
			self.numRows()
			self.numColumns()
			self.numCols()

		# Example
			>>> m = matrix([[1, 2],
			... 			[3, 4],
			... 			[5, 6]])
			>>> m.size
			(3, 2)
		"""
		return (self.numRows, self.numCols)
	
	def row(self, n):
		"""
		Returns a list of items in row n
		
		# Parameters
			n : int
				The index of the row which will be retrived
		
		# Returns
			An list of items in the nth row
		
		# See Also
			self.col()
			self.column()
			self.cols()
			self.columns()
			self.rows()

		# Example
			>>> m = matrix([[1, 2],
			... 			[3, 4])
			>>> m.column(0)
			[1, 2]
		"""
		if n > self.numRows:
			raise Exception(n, "Index is out of range of matrix")
		return self.amatrix[n]
	
	def column(self, n):
		"""
		Returns a list of items in column n
		
		# Parameters
			n : int
				The index of the column which will be retrived
		
		# Returns
			An list of items in the nth column
		
		# See Also
			self.cols()
			self.columns()
			self.row()
			self.rows()

		# Example
			>>> m = matrix([[1, 2],
			... 			[3, 4])
			>>> m.column(0)
			[1, 3]
		"""
		if n > self.numCols:
			raise Exception(n, "Index is out of range of matrix")
		col = []
		for row in self.amatrix:
			col.append(row[n])
		return col
		
	col = column
	
	@property
	def rows(self):
		"""
		Returns a list of all rows in the matrix
		
		# Returns
			An list of lists of items in each row
			
		# See Also
			self.cols()
			self.columns()
			self.col()
			self.column()
			self.row()

		# Example
			>>> m = matrix([[1, 2],
			... 			[3, 4])
			>>> m.columns()
			[[1, 2], [3, 4]]
		"""
		a = []
		for i in range(self.numRows):
			a.append(self.row(i))
		return a
	
	@property
	def columns(self):
		"""
		Returns a list of all columns in the matrix
		
		# Returns
			An list of lists of items in each column
		
		# See Also
			self.cols()
			self.rows()
			self.col()
			self.column()
			self.row()

		# Example
			>>> m = matrix([[1, 2],
			... 			[3, 4])
			>>> m.columns()
			[[1, 3], [2, 4]]
		"""
		a = []
		for i in range(self.numCols):
			a.append(self.col(i))
		return a
	
	cols = columns 
	
	@property
	def sum(self):
		"""
		Returns the sum of all elements in the matrix
		
		# Returns
			A number (int, float..)

		# Example
			>>> m = matrix([[1, 2],
			... 			[3, 4])
			>>> m.sum()
			10
		"""
		s = 0
		for row in self.amatrix:
			for item in row:
				s += item
		return s			
	
	def flatten(self):
		"""
		Flatens the matrix into a 1xn matrix

		# Example
			>>> m = matrix([[1, 2],
			... 			[3, 4])
			>>> m.flatten()
			>>> print(m)
			[1, 2, 3, 4]
		"""
		self.reshape((1, len(self)))
	
	def tolist(self):
		"""
		Returns the matrix in nested list form
		
		# See Also
			flatten()

		# Example
			>>> m = matrix([[1, 2],
			... 			[3, 4])
			>>> m.toList(s)
			[[1, 2], [3, 4]]
		"""
		return self.amatrix
		
	def reshape(self, s):
		"""
		Reshapes the matrix into new size

		# Parameters
			m : matrix object
			s : tuple (number of rows, number of columns)

		# See Also
			shape()

		# Example
			>>> m = matrix([[1, 2],
			... 			[3, 4])
			>>> s = (4, 1)
			>>> m.shape(s)
			>>> print(m)
			[[1],
			 [2],
			 [3],
			 [4]]
		"""
		self = shape(self, s)
		
