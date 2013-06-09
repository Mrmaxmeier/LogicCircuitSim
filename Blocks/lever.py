from guiblock import GuiBlock


class Lever(GuiBlock):
	"""UserInput."""
	def __init__(self):
		GuiBlock.__init__(self)
		self.ticks = 1
		self.inputs = {}
		self.outputs = {"Output":0}
		self.oldinputs = self.inputs
		self.texture = "leveroff.png"
		self.name = "Lever"
		self.bool = False
	def computeOutputs(self, inputs):
		"""...bei einem Update..."""
		outputs = self.outputs
		outputs["Output"] = self.bool
		return outputs
	def onClick(self):
		print("Lever ",self," was clicked.")
		if self.bool:
			self.bool = False
		else:
			self.bool = True
		self.computeOutputs(self.inputs)

avalibleblocks.append(["Lever",Lever,1])

