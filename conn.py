from getColor import *

class Connection(object):
	"""ein Kabel von Output zu Input - A zu B"""
	def __init__(self, output, input):
		self.output = output
		self.input = input
		self.bool = -1
	def update(self):
		out, outName = self.output
		inp, inpName = self.input
		self.bool = out.outputs[outName]
		inp.inputs[inpName] = self.bool
	
	def draw(self, canvas):
		def getPoint(l):
			return (l.winfo_rootx()-canvas.winfo_rootx(), l.winfo_rooty()-canvas.winfo_rooty())
		out, outName = self.output
		x1, y1 = getPoint(out.frame.outLabels[outName])
		inp, inpName = self.input
		x2, y2 = getPoint(inp.frame.inLabels[inpName])
		print( x1, y1, x2, y2)
		id = canvas.create_line(x1, y1, x2, y2, fill=standardCols(self.bool), width=3)
		canvas.tag_bind(id, "<ButtonPress>", self.click)
		return id
	
	def click(self, ev):
		from sim import Simulator as S
		if S.sim.selectedTool == "del":
			print("conn clicked!", S.sim.selectedTool)
			S.sim.connections.remove(self)
