# Define class
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")

# Create an object for class
give_me_a_car = Car()
give_me_a_yugo = Yugo()

# Print the object of class
print(give_me_a_car.exclaim())
print(give_me_a_yugo.exclaim())

class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

print(person)
print(doctor)
print(lawyer)