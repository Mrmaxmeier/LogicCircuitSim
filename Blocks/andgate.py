from guiblock import GuiBlock


class And(GuiBlock):
	"""AndGatter."""
	def __init__(self):
		GuiBlock.__init__(self)
		self.ticks = 1
		self.inputs = {"Input1":-1,"Input2":-1}
		self.outputs = {"Output":-1}
		self.oldinputs = self.inputs
		self.texture = "AND.gif"
		self.name = "AND"
	def computeOutputs(self, inputs):
		"""...bei einem Update..."""
		outputs = self.outputs
		if inputs["Input1"] == 1 and inputs["Input2"] == 1:
			outputs["Output"] = True
		else:
			outputs["Output"] = False
		return outputs
