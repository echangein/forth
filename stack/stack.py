class Stack:
	stack = []
	
	#def __init__(self):
	#	self.stack = stack
	
	def push(self, val = None):
		self.stack.append(val)
		
	
	def pop(self):
		return self.stack.pop()
	
	def drop(self):
		self.stack.pop()
