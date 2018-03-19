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
        print("%s You have lost 20 health" % self.health)
        self.health = self.health - 20


class Key(Item):
    def __init__(self, name, value):
        super(Key, self).__init__(name, value)
   
    def locked(self):
        print("The Door Is Locked")

    def open(self):
        print("The Door Is now unlocked")


class Potion(Item):
    def __init__(self, name, value):
        super(Potion, self).__init__(name, value)

    def drink(self):
        print("%s You drank a potion and gained 20 health" % self.health)
        self.health = self.health + 20


class Armour(Item):
    def __init__(self, name, value, durability ):
        super(Armour, self).__init__(name, value, durability)
        self.durability = 100

    def durability_damage(self):
        print("%s you have lost 2 hearts"% self.durability)
        self.durability = self.durability - 2