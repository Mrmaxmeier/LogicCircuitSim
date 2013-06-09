from conn import *
import pickle
from tkinter.filedialog import *


class Simulator:
	sim = None
	
	def __init__(self):
		self.connections = []
		self.blocks = []
		self.newconnection = {"Input":None,"Output":None}
	
	def tick(self):
		for block in self.blocks: block.onTick()
		for con in self.connections: con.update()
	
	def addBlock(self, block):
		self.blocks.append(block)
	
	def connect(self, output, input):
		"""output: (block, outputname)
		   input:  (block, inputname)"""
		self.disconnectAt(input)
		self.connections.append(Connection(output, input))
	
	def disconnectAt(self, input):
		(block, inpName) = input
		for con in self.connections:
			(cBlock, cInpName) = con.input
			if cBlock is block and cInpName == inpName:
				self.connections.remove(con)
	
	def save(self):
		with asksaveasfile() as f:
			pickle.dump(self, f)

def loadSim():
	with askopenfile() as f:
		return pickle.load(f)
