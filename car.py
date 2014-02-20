class Car(object):
	def __init__(self, weight, color, transmission, name):
		self.weight = weight
		self.color = color 
		self.transmission = transmission 
		self.name = name
		self.speed = 0

	def __repr__(self):
		return "{0} {1}".format(self.name, self.color)

	def accelerate(self):
		self.speed += 10



class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age 

	def __repr__(self):
		return "Person: {0}".format(self.name) 


my_car = Car(2000, "red", "manual")
my_car.weight
my_car.color
my_car.transmission


class NamedObject(object):
	def __init__(self, name):
		self.name = name

class Car(object):
	def __init__(self, weight, color, transmission, name):
		self.weight = weight
		self.color = color
		self.transmission = transmission 
		self.speed = 0

	def __repr__(self):
		return "Car: {0}".format(self.name)

	def accelerate(self):
		self.speed += 10

	def name(self):
		print "Baylee is a new sheriff in town"


class Person(namedObject):
	def __init__(self, name, age):
		self.age = age
		self.cars = []












