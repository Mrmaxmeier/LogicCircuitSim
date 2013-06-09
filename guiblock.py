import tkinter
from tkinter.dnd import *
from tkinter import *
from block import Block



def standardCols(val):
	if val == -1:
		return "red"
	elif val:
		return "green"
	else:
		return "black"



class GuiBlock(Block):
	def __init__(self):
		Block.__init__(self)
		self.name = "self.name"
		self.state = False
		self.canvas = self.frame = self.id = None
		self.coords = [0,0]
	
	def onTick(self):
		Block.onTick(self)
		self.GuiUpdate()
	
	def GuiUpdate(self):
		self.frame.updateIns(self.inputs)
		self.frame.updateOuts(self.outputs)
	
	def attach(self, canvas, x=10, y=10):
		if canvas is self.canvas:
			self.canvas.coords(self.id, x, y)
			return
		if self.canvas:
			self.detach()
		if not canvas:
			return
		frame = EpischerFrame(canvas,self.inputs,self.name,self.outputs)
		#label = tkinter.Label(canvas, text=self.name,
		#					  borderwidth=2, relief="raised")
		id = canvas.create_window(x, y, window=frame, anchor="nw")
		self.canvas = canvas
		#self.label = label
		self.frame = frame
		self.id = id
		#label.bind("<ButtonPress>", self.press)
		#frame.bind("<ButtonPress>", self.press)
		frame.label.bind("<ButtonPress>", self.press)
	
	def detach(self):
		canvas = self.canvas
		if not canvas:
			return
		id = self.id
		#label = self.label
		frame = self.frame
		#self.canvas = self.label = self.id = None
		self.canvas = self.frame = self.id = None
		canvas.delete(id)
		#label.destroy()
		frame.destroy()

	def press(self, event):
		if dnd_start(self, event):
			# where the pointer is relative to the label widget:
			self.x_off = event.x
			self.y_off = event.y
			# where the widget is relative to the canvas:
			self.x_orig, self.y_orig = self.canvas.coords(self.id)
		self.onClick()

	def move(self, event):
		x, y = self.where(self.canvas, event)
		self.canvas.coords(self.id, x, y)

	def putback(self):
		self.canvas.coords(self.id, self.x_orig, self.y_orig)

	def where(self, canvas, event):
		# where the corner of the canvas is relative to the screen:
		x_org = canvas.winfo_rootx()
		y_org = canvas.winfo_rooty()
		# where the pointer is relative to the canvas widget:
		x = event.x_root - x_org
		y = event.y_root - y_org
		# compensate for initial pointer offset
		return x - self.x_off, y - self.y_off

	def dnd_end(self, target, event):
		pass

class EpischerFrame(Frame):
	def __init__(self, parent, ins, text, outs):
		Frame.__init__(self, parent)
		self.label = Label(self, text=text,borderwidth=2, relief="raised")
		
		self.topFrame = Frame(self)
		self.inLabels = self.fill(self.topFrame, ins)
		self.bottomFrame = Frame(self)
		self.outLabels = self.fill(self.bottomFrame, outs)
		
		self.topFrame.pack(side="top", fill="both")
		self.bottomFrame.pack(side="bottom", fill="both")
		self.label.pack()
		
		self.pack()
	
	def fill(self, frame, names):
		res = {}
		for name in names:
			label = Label(frame, text=name)
			label.pack(side="left", expand="true")
			res[name] = label
		return res
	
	def updateColors(self, f, vals, labels):
		for key in labels.keys():
			val = vals[key]
			label = labels[key]
			label.config(foreground=f(val))
	
	def updateIns(self, vals): self.updateColors(standardCols, vals, self.inLabels); print(vals)
	def updateOuts(self, vals): self.updateColors(standardCols, vals, self.outLabels)
