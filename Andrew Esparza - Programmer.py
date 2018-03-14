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

    def name_tag(self):
        print("Tells Us All of your information")


class Programmer(Employee):
    def __init__(self, name, age, length, weight):
        super(Programmer, self).__init__(name, age, length)
        self.weight = weight


    def experience_recemmended(self):
        print("10 years")
