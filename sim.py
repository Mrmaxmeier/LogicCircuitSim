from conn import *
import pickle
from tkinter.filedialog import *
from tkinter import *

class Simulator:
	sim = None
	
	def __init__(self):
		self.connections = []
		self.blocks = []
		self.connImgs = []
		self.newconnection = {"Input":None,"Output":None}
		self.selectedTool = None#"del","select","dnd"
		self.selectedBlock = None
		self.settingswindow = None
		#self.maincanvas = None
	
	def lateinit(self, tk):
		if self.settingswindow:
			self.settingswindow.destroy()
		self.settingswindow = Settingswindow(tk)
	
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
		self.settingswindow.destroy()
	
	def after_load(self, canvas):
		self.settingswindow = Settingswindow(canvas._root())
		for block in self.blocks:
			block.attach(canvas, *block.coords)
		self.drawConns(canvas)
	def updateSettingswindow(self):
		print("Reloading SettingsWindow...")
		self.settingswindow.block_Selected(self.selectedBlock)
	
	def __getstate__(self):
		d = dict(self.__dict__)
		del d["settingswindow"]
		return d
		

def loadSim(canvas):
	with askopenfile("rb") as f:
		sim = pickle.load(f)
		sim.after_load(canvas)
		#sim.maincanvas = canvas
		Simulator.sim.destroy(canvas)
		Simulator.sim = sim




class Settingswindow():
	"""Das Einstellungsfenster"""
	def __init__(self, tk):
		self.selectedBlock = Simulator.sim.selectedBlock
		self.root = Toplevel(tk)
		self.root.title("Settings")
		self.widgets = []
		self.contents = []
		self.labels = []
		self.textVars = []
	def block_Selected(self, block):
		self.selectedBlock = block
		self.updateGui()
	def updateGui(self):
		self.settings = self.selectedBlock.settings #"Name":[Val,von,bis]
		self.clearGui()
		for name in self.settings.keys():
			#print(name)
			textvar = StringVar(self.root)
			textvar.set(self.settings[name][0])
			lab = Label(self.root, text = name)
			spin = Spinbox(self.root, from_ = self.settings[name][1], to = self.settings[name][2],textvariable=textvar)
			
			lab.pack()
			spin.pack()
			self.labels.append(lab)
			self.contents.append(lab)
			self.contents.append(spin)
			self.widgets.append((name, spin))
			self.textVars.append(textvar)
		self.updateButton = Button(self.root, command=lambda : Simulator.sim.settingswindow.onChange(), text="Update Block")
		self.contents.append(self.updateButton)
		self.updateButton.pack()
	def clearGui(self):
		for widget in self.contents:
			widget.destroy()
		self.contents = []
		self.widgets = []
	def onChange(self):
		for name, widget in self.widgets:
			self.settings[name] = widget.get()
		print(self.settings)
		#for widget,setting in self.widgets,self.settings.keys():
		#	self.settings[setting][0] = widget.get()
		self.updateBlock()
	def updateBlock(self):
		self.selectedBlock.settings = self.settings
		self.selectedBlock.onSetting()
	def destroy(self):
		self.root.destroy()
