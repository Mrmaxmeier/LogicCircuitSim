class Connection(object):
	"""ein Kabel von Output zu Input - A zu B"""
	def __init__(self, a, output, b, input):
		self.a,self.output = a, output
		self.b,self.input = b, input
		self.bool = None
	def update(self):
		self.bool =self.a.outputs[self.output]
		self.b.inputs[self.input] = self.bool 