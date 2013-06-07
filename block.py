class Block():
	"""BlockKlasse"""
	def __init__(self):
		self.ticks = 1
		self.inputs = {"Input":-1}
		self.outputs = {"Output":-1}
		self.oldinputs = self.inputs
		self.texture = ""
		self.name = "Dummy"
	def onTick(self):
		"""...bei einem tick..."""
		if self.oldinputs != self.inputs:
			self.outputs = self.onUpdate(self.inputs,self.outputs)
		self.oldinputs = self.inputs
	def computeOutputs(self, self.inputs, self.outputs):
		"""...bei einem Update..."""
		return self.outputs
	def onClick(self):
		self.computeOutputs()