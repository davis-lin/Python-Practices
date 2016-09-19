class Car():
    pass

class Yugo():
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()



class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()

print(give_me_a_car.exclaim())
print(give_me_a_yugo.exclaim())