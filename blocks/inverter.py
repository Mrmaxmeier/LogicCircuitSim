from block import Block

class Inverter(Block):
	"""Invertiert das Input."""
	def __init__(self):
		self.ticks = 1
		self.inputs = {"Input":-1}
		self.outputs = {"Output":-1}
		self.texture = "NOT.gif"
		self.name = "Inverter"
	def computeOutputs(self, inputs, outputs):
		"""...bei einem Update..."""
		if self.inputs["Input"] == 0:
			self.outputs["Output"] = 1
		if self.inputs["Input"] == 1:
			self.outputs["Output"] = 1
		return self.outputs
