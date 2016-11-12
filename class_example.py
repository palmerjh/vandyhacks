class Person(object):
	number_noses = 1
	"""docstring for Person"""
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

class Hacker(Person):
	"""docstring for Hacker"""
	def __init__(self, name, *projects):
		super(Hacker, self).__init__(name)
		self.projects = projects
		self.number_redbulls_dranken = 0

	def drinkRedBull(self,number=7):
		self.number_redbulls_dranken += number
		

Joey = Hacker('joey',['nothing'])
Joey.drinkRedBull()
print Joey.number_redbulls_dranken # prints 7
Joey.drinkRedBull(10)
print Joey.number_redbulls_dranken # prints 17

print Joey.number_noses


		