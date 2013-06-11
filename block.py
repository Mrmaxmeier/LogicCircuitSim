class Block():
	"""BlockKlasse"""
	def __init__(self):
		self.ticks = 1
		self.inputs = {"Input":-1}
		self.outputs = {"Output":-1}
		self.oldinputs = self.inputs
		self.texture = ""
		self.name = "Dummy"
		self.settings = {}#"Name":[Val,von,bis]
	def onSetting(self):
		pass
	def onTick(self):
		"""...bei einem tick..."""
		#print(self.oldinputs,self.inputs)
		#if self.oldinputs == self.inputs:
		#	pass
		#else:
		#	self.outputs = self.computeOutputs(self.inputs)
		#self.oldinputs = self.inputs
		self.outputs = self.computeOutputs(self.inputs)
	def computeOutputs(self, inputs):
		"""...bei einem Update..."""
		outputs = self.outputs
		return outputs
	def onClick(self):
		self.computeOutputs(self.inputs)