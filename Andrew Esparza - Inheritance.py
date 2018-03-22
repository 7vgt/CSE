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
        print("%s you have lost 2 hearts" % self.durability)
        self.durability = self.durability - 2


class Weapon(Item):
    def __init__(self, name, value):
        super(Weapon, self).__init__(name, value)
        self.durability = 100
        self.attack = 1
        self.enemy = 10

    def deal_damage(self):
        print("%s You have hit someone and taken 1 heat from them" % self.enemy)
        self.enemy = self.enemy - 1


class Blocks(Item):
    def __init__(self, name, value):
        super(Blocks, self).__init__(name, value)

    def place(self):
        print("You have placed a block in front of you")

    def destroy(self):
        print("You Have Broken a block in front of you")


class Draw(Item):
    def __init__(self, name, value):
        super(Draw, self).__init__(name, value)

    def doodle(self):
        print("you drew something out of this world")

    def erase(self):
        print("The paper is now empty and has nothing on it now")


class Character(Item):
    def __init__(self, name, value):
        super(Character, self).__init__(name, value)

    def information(self):
        print("This has lots of random facts on it")


class Inventory(Item):
    def __init__(self, name, value):
        super(Inventory, self).__init__(name, value)

    def hold(self):
        print("you are holding on to your items")


class Dishes(Item):
    def __init__(self, name, value):
        super(Dishes, self).__init__(name, value)

    def throw(self):
        print("You shattered the Item ")


class Ac(Item):
    def __init__(self, name, value):
        super(Ac, self).__init__(name, value)

    def cold(self):
        print("The room suddenly got cold")

    def hot(self):
        print("The room got really hot all of a sudden")
        

class Clock(Item):
    def __init__(self, name, value, time):
        super(Clock, self).__init__(name, value)
        self.time = time
        
    def clock_read(self):
        print("You should have learn how to read time")
        

class clothes(Item):
    def __init__(self, name, value, brand):
        super(clothes, self).__init__(name, value)
        self.brand = brand
        
    def wear(self):
        print("It snuggly fits you")


class Radio(Item):
    def __init__(self, name, value):
        super(Radio, self).__init__(name, value)

    def singing(self):
        print("Have Mercuyyyy on my heartt....")
