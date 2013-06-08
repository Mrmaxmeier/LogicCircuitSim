from guiblock import GuiBlock

class Inverter(GuiBlock):
	"""Invertiert das Input."""
	def __init__(self):
		GuiBlock.__init__(self)
		self.ticks = 1
		self.inputs = {"Input":-1}
		self.outputs = {"Output":-1}
		self.oldinputs = self.inputs
		self.texture = "NOT.gif"
		self.name = "Inverter"
	def computeOutputs(self, inputs):
		"""...bei einem Update..."""
		outputs = self.outputs
		if inputs["Input"] == 0:
			outputs["Output"] = True
		if inputs["Input"] == 1:
			outputs["Output"] = False
		return outputs
