from block import Block

class Lamp(Block):
	"""Eine Info LED."""
	def __init__(self):
		self.ticks = 1
		self.inputs = {"Input":-1}
		self.outputs = {}
		self.oldinputs = self.inputs
		self.texture = "lamp.png"
		self.name = "Lamp"
	def computeOutputs(self, inputs):
		"""...bei einem Update..."""
		outputs = self.outputs
		if self.inputs["Input"] == 0:
			print("Lamp ",self," turned Off.")
			self.texture = "lampoff.png"
		if self.inputs["Input"] == 1:
			print("Lamp ",self," turned On.")
			self.texture = "lampon.png"
		return outputs
