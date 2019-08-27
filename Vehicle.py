# define the Vehicle class
class Vehicle:    
	name = ""    
	kind = "car"    
	color = ""   
	value = 100.00    
	def description(self):        
		desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)        
		return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Toyota"
car1.kind = "car"
car1.value = 20000

car2 = Vehicle()
car2.name = "Ford"
car2.kind = "pickup"
car2.value = 30000
# test code

print(car1.description())
print(car2.description())
