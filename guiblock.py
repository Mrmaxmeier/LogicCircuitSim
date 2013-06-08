import tkinter
from tkinter.dnd import *

from block import Block

class GuiBlock(Block):
	def __init__(self):
		Block.__init__(self)
		self.name = "self.name"
		self.state = False
		self.canvas = self.label = self.id = None
		self.coords = [0,0]

	def attach(self, canvas, x=10, y=10):
		if canvas is self.canvas:
			self.canvas.coords(self.id, x, y)
			return
		if self.canvas:
			self.detach()
		if not canvas:
			return
		label = tkinter.Label(canvas, text=self.name,
							  borderwidth=2, relief="raised")
		id = canvas.create_window(x, y, window=label, anchor="nw")
		self.canvas = canvas
		self.label = label
		self.id = id
		label.bind("<ButtonPress>", self.press)

	def detach(self):
		canvas = self.canvas
		if not canvas:
			return
		id = self.id
		label = self.label
		self.canvas = self.label = self.id = None
		canvas.delete(id)
		label.destroy()

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