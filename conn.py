class Connection(object):
	"""ein Kabel von Output zu Input - A zu B"""
	def __init__(self, output, input):
		self.output = output
		self.input = input
		self.bool = None
	def update(self):
		out, outName = self.output
		inp, inpName = self.input
		self.bool =self.a[0].outputs[self.a[1]]
		self.b[0].inputs[self.b[1]] = self.bool 
