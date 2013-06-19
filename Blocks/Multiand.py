from guiblock import GuiBlock


class MultiAnd(GuiBlock):
	"""AndGatter."""
	def __init__(self):
		GuiBlock.__init__(self)
		self.ticks = 1
		self.inputs = {"Input1":-1,"Input2":-1}
		self.outputs = {"Output":-1}
		self.oldinputs = self.inputs
		self.texture = "AND.gif"
		self.name = "AND"
		self.settings = {"Inputs":[2,2,99]}#"Name":[Val,von,bis]
	def onSetting(self):
		self.inputs = {}
		for c in range(int(self.settings["Inputs"][0])):
			inputname = "I"+str(c+1)
			self.inputs[inputname] = -1
	def computeOutputs(self, inputs):
		"""...bei einem Update..."""
		outputs = self.outputs
		c = 0
		for input in inputs.values():
			if input:
				c += 1
		if c == len(inputs.values()):
			outputs["Output"] = True
		else:
			outputs["Output"] = False
		return outputs

avalibleblocks.append(["MultiAnd",MultiAnd,1])

