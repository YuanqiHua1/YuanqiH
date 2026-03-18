from person import Person

class Teacher(Person):
	def __init__(self,firstname,lastname,course):
		super().__init__(firstname,lastname)
		self.course = course

	def introduce(self):
		return f'{super().introduce()} \nCourse: {self.course}'
