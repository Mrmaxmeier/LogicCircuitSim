#!/usr/bin/python3

from tkinter import *

def standardCols(val):
	if val == -1:
		return "red"
	elif val:
		return "green"
	else:
		return "black"

class EpischerFrame(Frame):
	def __init__(self, parent, ins, text, outs):
		Frame.__init__(self, parent)
		self.label = Label(self, text=text)
		
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
	
	def updateIns(self, vals): self.updateColors(standardCols, vals, self.inLabels)
	def updateOuts(self, vals): self.updateColors(standardCols, vals, self.outLabels)

root = Tk()
f=EpischerFrame(root, ["lol", "rofl", "kopter"], "hallo", range(10))
f.updateIns({"lol":-1, "rofl":1, "kopter":0})
root.mainloop()
