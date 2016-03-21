#!/usr/bin/env python
#-*-coding:utf-8-*-

from stack import Stack

class Forth:

	FLASHSIZE = 4 * 1024
	RAMSIZE = 2 * 1024

	def __init__(self):
		self.flash = [0 for i in range(self.FLASHSIZE)]
		self.ram = [0 for i in range(self.RAMSIZE)]

		#S		data stack pointer
		#RP		return stack pointer

		self.IP = 0	#interpretner pointer
		self.W = 0 	#curren word pointer

		self.DataStack = Stack()
		self.ReturnStack = Stack()
		
		self.flash[0] = self.lit
		self.flash[1] = 66
		self.flash[2] = self.dot
		self.flash[3] = self.halt

	def getAddr(self, worldName):
		return 0

	def halt(self):
		print('System halted')
		exit(-1)

	def d_to_r(self):
		#	>r	move value from data stack to return stack
		self.ReturnStack.push(self.DataStack.pop())
	
	def r_to_d(self):
		# 	r>	move value from return stack to data stack
		self.DataStack.push(self.ReturnStack.pop())
		
	def r_get(self):
		# r@	copy value from return stack to data stack
		tmp = self.ReturnStack.pop()
		self.DataStack.push(tmp)
		self.ReturnStack.push(tmp)
	
	def ram_get(self):
		#	@ get from ram
		addr = self.DataStack.pop()
		self.DataStack.push(self.ram[addr])
		
	def ram_put(self):
		#	@ get from ram
		addr = self.DataStack.pop()
		val = self.DataStack.pop()
		self.ram[addr] = val
	
	def lit(self):
		self.IP += 1
		self.DataStack.push(self.flash[self.IP])
		
	def dot(self):
		print(self.DataStack.pop())

# ===================== forth engine =====================
		
	def run(self):
		if hasattr(self.flash[self.IP], '__call__'):
			self.flash[self.IP]()
			self.IP += 1
		else:
			self.ReturnStack.push(self.IP)
			self.IP = self.flash[self.IP]
	
	def start(self, startWord = 'QUIT'):
		self.IP = self.getAddr(startWord)
		
		while True:
			self.run()

# ===================== forth engine =====================

#forth = Forth()
#forth.start()

		
def tst():
	print('tst')
		
ss = 'hello'
print(ord(ss[0]))

print(chr(8)+ss[0]),
print(chr(8)+ss[1]),
