from conn import *

class Simulator:
	def __init__(self):
		self.connections = []
		self.blocks = []
	
	def tick(self):
		for block in self.blocks: block.onTick()
		for con in self.connections: con.update()
	
	def addBlock(self, block):
		self.blocks.append(block)
	
	def connect(self, output, input):
		"""output: (block, outputname)
		   input:  (block, inputname)"""
		self.disconnectAt(input)
		self.connections.append(Connection(output, input)
	
	def disconnectAt(self, (block, inpName)):
		for con in self.connections:
			(cBlock, cInpName) = con.input
			if cBlock is block and cInpName == inpName:
				self.connections.remove(con)
