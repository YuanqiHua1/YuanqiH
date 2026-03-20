class Person:
	def __init__(self,firstname,lastname):
		self.firstname = firstname
		self.lastname = lastname

	def introduce(self):
		return f'Name : {self.firstname}{self.lastname}'
