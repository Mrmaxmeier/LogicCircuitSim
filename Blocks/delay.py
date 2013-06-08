from guiblock import GuiBlock


class Delay(GuiBlock):
	"""1Tick Delay."""
	def __init__(self):
		GuiBlock.__init__(self)
		self.ticks = 1
		self.inputs = {"Input":-1}
		self.outputs = {"Output":-1}
		self.oldinputs = self.inputs
		self.texture = "AND.gif"
		self.name = "AND"
	def computeOutputs(self, inputs):
		"""...bei einem Update..."""
		outputs = self.outputs
		
		outputs["Output"] = inputs["Input"]
		
		return outputs
