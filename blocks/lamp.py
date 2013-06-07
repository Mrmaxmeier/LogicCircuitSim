class Lamp(Block):
	"""Eine Info LED."""
	def __init__(self):
		self.ticks = 1
		self.inputs = {"Input":-1}
		self.outputs = {}
		self.texture = "lamp.png"
		self.name = "Lamp"
	def computeOutputs(self, self.inputs, self.outputs):
		"""...bei einem Update..."""
		if self.inputs["Input"] = 0:
			self.texture = "lampoff.png"
		if self.inputs["Input"] = 1:
			self.texture = "lampon.png"
		return self.outputs
