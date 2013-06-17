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
		self.selectedTool = None#"del","select","dnd"
		self.selectedBlock = None
		#self.maincanvas = None
	
	def tick(self):
		for block in self.blocks: block.onTick()
		for con in self.connections: con.update()
	
	def addBlock(self, block):
		self.blocks.append(block)
	
	def deleteBlock(self, block):
		#print(block.frame._root().__dict__)
		del block.frame._root()._DndHandler__dnd
		
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
		
	def mkConn(self):
		print("Making connection: ", self.newconnection)
		self.connect(self.newconnection["Output"], self.newconnection["Input"])
		self.newconnection = {"Input":None,"Output":None}
	
	def disconnectAt(self, input):
		(block, inpName) = input
		for con in self.connections:
			(cBlock, cInpName) = con.input
			if cBlock is block and cInpName == inpName:
				self.connections.remove(con)
	
	def save(self):
		with asksaveasfile("wb") as f:
			pickle.dump(self, f)
	
	def clearConns(self, canvas):
		for line in self.connImgs:
			canvas.delete(line)
		self.connImgs = []
	
	def drawConns(self, canvas):
		self.clearConns(canvas)
		for conn in self.connections:
			self.connImgs.append(conn.draw(canvas))
	
	def destroy(self, canvas):
		for block in self.blocks:
			block.detach()
		self.clearConns(canvas)
	
	def after_load(self, canvas):
		for block in self.blocks:
			block.attach(canvas, *block.coords)
			self.drawConns(canvas)

def loadSim(canvas):
	with askopenfile("rb") as f:
		sim = pickle.load(f)
		sim.after_load(canvas)
		#sim.maincanvas = canvas
		Simulator.sim.destroy(canvas)
		Simulator.sim = sim
