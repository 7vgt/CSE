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
    def __init__(self, name, value):
        super(Armour, self).__init__(name, value)
        self.durability = 100

    def durability_damage(self):
        print("%s you have lost 2 hearts"% self.durability)
        self.durability = self.durability - 2


class Weapon(Item):
    def __init__(self, name, value):
        super(Weapon, self).__init__(name, value)
        self.durability = 100
        self.attack = 1
        self.enemy = 10

    def deal_damage(self):
        print("%s You have hit someone and taken 1 heat from them"% self.enemy)
        self.enemy = self.enemy - 1


class blocks(Item):
    def __init__(self, name, value):
         super(blocks, self).__init__(name, value)

    def Place(self):
        print("You have placed a block in front of you")

    def Break(self):
        print("You Have Broken a block in front of you")


class draw(Item):
    def __init__(self, name, value):
        super(draw, self).__init__(name, value)

    def Doodle(self):
        print("you drew something out of this world")

    def Erase(self):
        print("The paper is now empty and has nothing on it now")

class Files(Item):
    def __init__(self, name, value):
        super(Files, self).__init__(name, value)

    def information(self):
        print("This has lots of random facts on it")

class Inventory(Item):
    def __init__(self, name, value):
        super(Inventory, self).__init__(name, value)

    def Hold(self):
        print("you are holding on to your items")

class Dishes(Item):
    def __init__(self, name, value):
        super(Dishes, self).__init__(name, value)

    def Throw(self):
        print("You shattered the Item ")

class Ac_unit(Item):
    def __init__(self, name, value):
        super(Ac_unit, self).__init__(name, value)

    def Cold(self):
        print("The room suddenly got cold")

    def Hot(self):
        print("The room got really hot all of a sudden")
        
class Clock(Item):
    def __init__(self, name, value, time):
        super(Clock, self).__init__(name, value)
        self.time = time
        
    def Clock_read(self):
        print("You should have learn how to read time")
        
class clothes(Item):
    def __init__(self, name, value, brand):
        super(clothes, self).__init__(name, value)
        self.brand = brand
        
    def wear(self):
        print("It snuggly fits you")
        
class Bake(Item):
    def __init__(self):
        super(Bake, self).__init__()