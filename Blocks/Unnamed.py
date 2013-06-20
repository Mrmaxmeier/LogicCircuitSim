from guiblock import GuiBlock


class Unnamed(GuiBlock):
  """WIP BLOCK."""
	def __init__(self):
		GuiBlock.__init__(self)
		self.ticks = 1
		self.inputs = {"Input":-1}
		self.outputs = {"Output":-1}
		self.oldinputs = self.inputs
		self.name = "WIP"
		self.settings = {"Name":[5,1,99]}#"Name":[Val,von,bis]
		self.time = 0
	def onSetting(self):
		self.name = int(self.settings["Name"][0])
	def computeOutputs(self, inputs):
		"""...bei einem Update..."""
		outputs = self.outputs
    outputs["Output"] = self.inputs["Input"]
		return outputs

avalibleblocks.append(["WIP",Unnamed,1])
