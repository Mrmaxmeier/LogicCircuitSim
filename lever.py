from block import Block
class Lever(Block):
	"""UserInput."""
	def __init__(self):
		self.ticks = 1
		self.inputs = {}
		self.outputs = {"Output":0}
		self.texture = "leveroff.png"
		self.name = "Switch"
		self.bool = False
	def computeOutputs(self, inputs, outputs):
		"""...bei einem Update..."""
		self.outputs["Output"] = self.bool
		return self.outputs
	def onClick(self):
		if self.bool:
			self.bool = 0
		else:
			self.bool = 1
		self.computeOutputs()
