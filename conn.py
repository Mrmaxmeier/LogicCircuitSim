class Connection(object):
	"""ein Kabel von Output zu Input - A zu B"""
	def __init__(self, output, input):
		self.output = output
		self.input = input
		self.bool = None
	def update(self):
		out, outName = self.output
		inp, inpName = self.input
		self.bool = out.outputs[outName]
		inp.inputs[inpName] = self.bool 
