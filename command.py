class Command(object):
	def __init__(self, name, numParam, code):
		self.name = name
		self.numParam = numParam
		self.code = code

	def getNumParams(self):
		return self.numParam

	def getName(self):
		return self.name

	def getCode(self):
		return self.code

	def generate(self, params):
		if len(params) != getNumParams:
			print("Number of inputs and parameters incorrect")