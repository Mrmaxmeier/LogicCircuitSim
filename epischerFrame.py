#!/usr/bin/python3

from tkinter import *

class EpischerFrame(Frame):
	def __init__(self, parent, ins, text, outs):
		Frame.__init__(self, parent)
		self.label = Label(self, text=text)
		
		self.topFrame = Frame(self)
		self.inLabels = self.fill(self.topFrame, ins)
		self.bottomFrame = Frame(self)
		self.outLabels = self.fill(self.bottomFrame, outs)
		
		self.topFrame.pack(side="top")
		self.bottomFrame.pack(side="bottom")
		self.label.pack()
		
		self.pack()
	
	def fill(self, frame, names):
		res = {}
		for name in names:
			label = Label(frame, text=name)
			label.pack(side="left")
			res[name] = label
		return res

root = Tk()
EpischerFrame(root, ["lol", "rofl"], "hallo", range(10))
root.mainloop()
