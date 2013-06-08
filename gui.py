import tkinter
from tkinter.dnd import *


from test import *


class GuiBlock:
	def __init__(self, block):
		self.block = block
		self.name = self.block.name
		self.state = False
		self.canvas = self.label = self.id = None

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
		self.block.onClick()

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



def gui():
	root = tkinter.Tk()
	root.geometry("+1+1")
	tkinter.Button(command=root.quit, text="Quit").pack()
	tkinter.Button(command=tickandstatus, text="Tick").pack()
	t1 = Tester(root)
	t1.top.geometry("+1+60")
	#t2 = Tester(root)
	#t2.top.geometry("+120+60")
	#t3 = Tester(root)
	#t3.top.geometry("+240+60")
	
	
	
	
	i1 = GuiBlock(lever)
	i2 = GuiBlock(inverter)
	i3 = GuiBlock(lamp)
	i1.attach(t1.canvas)
	i2.attach(t1.canvas)
	i3.attach(t1.canvas)
	root.mainloop()
gui()