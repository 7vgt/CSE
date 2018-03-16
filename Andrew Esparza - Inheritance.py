class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def sell(self):
        print("%s You sold your item for" % self.value)


    def drop(self):
        print("you dropped your item")
        
        
class Food(Item):
    def __init__(self, name, value, health):
        super(Food, self).__init__(name, value)
        self.health = health

    def eat(self):
        print("%s You have gain 10 health"% self.health)
        self.health = self.health + 10

    def chock(self):
        print("%s You have lost 20 health"% self.health)
        self.health = self.health - 20
