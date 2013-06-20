from guiblock import GuiBlock


class TFlipFlop(GuiBlock):
	def __init__(self):
		GuiBlock.__init__(self)
		self.ticks = 1
		self.inputs = {"Input":-1, "set":False, "unset":False}
		self.outputs = {"Output":False}
		self.lastval = -1
		self.name = "T-Flip-Flop"
	def computeOutputs(self, inputs):
		"""...bei einem Update..."""
		outputs = self.outputs
		if self.lastval == 1 and inputs["Input"] == 0:
			outputs["Output"] = not outputs["Output"]
		self.lastval = inputs["Input"]
		if inputs["unset"]:
			outputs["Output"] = False
		if inputs["set"]:
			outputs["Output"] = True
		return self.outputs


avalibleblocks.append(["T-Flip-Flop",TFlipFlop,1])
