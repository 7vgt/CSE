class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s gose to work" % self.name)

class Employee(Person):
    def __init__(self, name, age, length):
        super(Employee, self).__init__(name, age)
        self.length = length


    def eye_color(self):
        print("You have blue eyes")


class Programmer(Employee):
    def __init__(self, name, age, length, weight):
        super(Programmer, self).__init__(name, age, length)
        self.weight = weight


    def birth(self):
        print("Your birthday is on November 17 2002")


Programmer
