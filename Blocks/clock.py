from guiblock import GuiBlock


class Clock(GuiBlock):
	"""Einstellbare Clock."""
	def __init__(self):
		GuiBlock.__init__(self)
		self.ticks = 1
		self.inputs = {}
		self.outputs = {"Output":-1}
		self.oldinputs = self.inputs
		self.name = "Clock"
		self.settings = {"An-Ticks":[5,1,99],"Aus-Ticks":[5,1,99]}#"Name":[Val,von,bis]
		self.onticks = 0
		self.offticks = 0
		self.time = 0
	def onSetting(self):
		self.onticks = int(self.settings["An-Ticks"][0])
		self.offticks = int(self.settings["Aus-Ticks"][0])
	def computeOutputs(self, inputs):
		"""...bei einem Update..."""
		outputs = self.outputs
		if self.time >= self.onticks + self.offticks:
			self.time = 0
		
		if self.time >= self.onticks:
			outputs["Output"] = True
		elif self.time < self.onticks:
			outputs["Output"] = False
		
		self.time += 1
		return outputs

avalibleblocks.append(["Clock",Clock,1])

