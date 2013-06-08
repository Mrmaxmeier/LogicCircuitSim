from block import Block
class Lever(Block):
	"""UserInput."""
	def __init__(self):
		self.ticks = 1
		self.inputs = {}
		self.outputs = {"Output":0}
		self.oldinputs = self.inputs
		self.texture = "leveroff.png"
		self.name = "Switch"
		self.bool = False
	def computeOutputs(self, inputs):
		"""...bei einem Update..."""
		outputs = self.outputs
		outputs["Output"] = self.bool
		return outputs
	def onClick(self):
		if self.bool:
			self.bool = False
		else:
			self.bool = True
		self.computeOutputs(self.inputs)
