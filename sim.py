from conn import *
import pickle
from tkinter.filedialog import *


class Simulator:
	sim = None
	
	def __init__(self):
		self.connections = []
		self.blocks = []
		self.connImgs = []
		self.newconnection = {"Input":None,"Output":None}
		self.selectedTool = None#"del","select"
		self.selectedBlock = None
	
	def tick(self):
		for block in self.blocks: block.onTick()
		for con in self.connections: con.update()
	
	def addBlock(self, block):
		self.blocks.append(block)
	
	def deleteBlock(self, block):
		self.blocks.remove(block)
		block.detach()
		for conn in self.connections:
			out, outName = conn.output
			inp, inpName = conn.input
			if out is block or inp is block:
				self.connections.remove(conn)
	
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
	
	def clearConns(self, canvas):
		for line in self.connImgs:
			canvas.delete(line)
		self.connImgs = []
	
	def drawConns(self, canvas):
		self.clearConns(canvas)
		for conn in self.connections:
			self.connImgs.append(conn.draw(canvas))

def loadSim():
	with askopenfile() as f:
		return pickle.load(f)
