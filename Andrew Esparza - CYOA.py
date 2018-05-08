class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def sell(self):
        print("%s You sold your item for" % self.value)

    def drop(self):
        print("you dropped your item")

    def PickUp(self):
        print('You picked up the Item' )


class Food(Item):
    def __init__(self, name, value, health):
        super(Food, self).__init__(name, value)
        self.health = 10

    def eat(self):
        print("%s You have gain 10 health" % self.health)
        self.health = self.health + 10

    def chock(self):
        print("%s You have lost 20 health" % self.health)
        self.health = self.health - 20


class Key(Item):
    def __init__(self, name, value):
        super(Key, self).__init__(name, value)

    def lockes(self):
        print("The Door Is Locked")

    def open(self):
        print("The Door Is now unlocked")


class Potion(Item):
    def __init__(self, name, value, effect):
        super(Potion, self).__init__(name, value)
        self.effect = effect

    def drink(self):
        print("%s You drank a potion and gained 20 health" % self.health)
        self.health = self.health + 20


class Armour(Item):
    def __init__(self, name, value, type):
        super(Armour, self).__init__(name, value)
        self.durability = 100
        self.type = type

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


class Tool(Weapon):
    def __init__(self, name, value):
        super(Tool, self).__init__(name, value,)


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


class Inventory(Item):
    def __init__(self, name, value):
        super(Inventory, self).__init__(name, value)

    def hold(self):
        print("you are holding on to your items")


class Ladder(Item):
    def __init__(self, name, value):
        super(Ladder, self).__init__(name, value)

    def climb(self):
        print("You have gone up the ladder ")


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


class Clothes(Item):
    def __init__(self, name, value, brand):
        super(Clothes, self).__init__(name, value)
        self.brand = brand

    def wear(self):
        print("It snugly fits you")


class Radio(Item):
    def __init__(self, name, value):
        super(Radio, self).__init__(name, value)

    def sing(self):
        print("(Song Lyrics)Just Have Mercy... on my heart...."
              "Can I take back And just star all over")


Apple = Food('Apple', '$1', 10)

Pizza = Food('Pizza', '$13.95', 25)

Cookie = Food('Cookie', '$2.50', 2)

cheese = Food('Cheese', '$100', 20)

Wishing_cake = Food('Wishing Cupcake', '$10,000', 100)

Candy = Food('Candy', '$1', 2)

Carrot = Food('Carrot', '$4', 5)

Pink_milk_shake = Food('Pink milk shake', '$5', 15)

Fries = Food('French Fries', '$2.50', 10)

Big_Mac = Food('Big Mac', '$5', 20)

BaJa_Blast = Food('BAJA Blast', '$5', 15)

Nacho_Fries = Food('Nacho Fries', '$1', 5)

Poutine = Food('Beef Poutine', '$10', 25)

Mc_Chicken = Food('McChicken', '$1.50', 10)

Pop_Corn = Food('PopCorn', '$1', 5)

Stone_blocks = Blocks('Stone block', '$5')

Wood_blocks = Blocks('Wood', '$5')

Gucci_shirt = Clothes('Gucci shirt', '$1000', 'Gucci')

Calvan_Kalin_Underwear = Clothes('Underwear', '$75', 'Calvin Kalin')

Levi_pants = Clothes('Skinny Jeans', '$50', 'Levis')

Hollister_Jacket = Clothes('Jacket', '$40', 'Hollister')

Addidas_Shoes = Clothes('Running suit', '$30', 'Hollister')

Yeezys_Shoes = Clothes('Shoes', '$400', 'Addidas')

Supreme_socks = Clothes('Socks', '$40', 'Supreme')

Front_Door_Key = Key('House Key', None)

Garage_key = Key('Garage Key', None)

Health_potion = Potion('Healing Potion', '$20', 'Healing')

Damage_potion = Potion('Damage Potion', '$30', 'Lost Health')

Iron_Helmet = Armour('Iron Helmet', '$40', 'Iron')

Iron_Chestplate = Armour('Iron Chestplate', '$80', 'Iron')

Iron_leggings = Armour('Iron Leggings', '$60', 'Iron')

Iron_Boots = Armour('Iron Boots', '$40', 'Iron')

Diamond_Helmet = Armour('Diamond Boots', '$1000', 'Diamond')

Diamond_Chestplate = Armour('Tier III ChestPlate', '$1400', 'Diamond')

Diamond_Leggings = Armour('Tier III leggings', '$1200', 'Diamond')

Diamond_Boots = Armour('Tier III Boots', '$1000', 'Diamond')

Wood_sword = Weapon('Tier III Sword', '$20')

stone_sword = Weapon('Stone Sword', '$40')

Gold_sword = Weapon('Gold Sword', '$120')

Steel_Sword = Weapon('Steel Sword', '$60')

Diamond_sword = Weapon('Excalibur', '$1000')

Pick_Axe = Tool('Pick Axe', '$250')

Legendary_Axe_Of_Amazing = Tool('Axe', '$500')

Code_Breaker = Tool('Axe', '$1000000')

TreeHouse_Ladder = Ladder('Tree House Ladder', None)

Trophy_end = Item('Trophy', 'Price less')


class Characters(object):
    def __init__(self, name, move, inventory, abilities, health, status, physique, description, money,
                 eat):
        self.name = name
        self.move = move
        self.inventory = inventory
        self.abilities = abilities
        self.health = 100
        self.status = status
        self.physique = physique
        self.description = description
        self.eat = eat
        self.take_damage = health - 1
        self.money = money

    def talk_to_person(self):
        if self.talk:
            self.talk = True
            print("Hi how are you")
        else:
            print("No response")

    def interaction(self):
        if self.interaction:
            self.interaction = True
            print("You: how are you")
            print("Random: Oh... good... bye")

    def attack_punch(self):
        if self.attack_punch:
            self.attack_punch = False
            print("You thought")
            attack = self.health - 1


Timmy = Characters('Timmy', None, ['Iron Boots', 'Iron Chestplate', 'Iron leggings'], 'Speed, Jump Boost, weakness',
                   100, 'Normal', '4ft 9in, 92P', 'He is kinda short with, blue eyes, buck teeth, And always'
                   'wearing a pink hat', None, 1000)

Vicky = Characters('Vicky', None, None, 'Speed', 1000, 'Speed', '5ft 9Inches', 'She has orange'
                   'hair with a burning look of anger that will frighten anyone', None, 0)


class Room(object):
    def __init__(self, name, north, south, east, west, items, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.items = items
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


VROOM = Room("Vicky's room", 'SECRETROOM', None, 'HALLWAY', None, ["Key", "Pizza"],
             "you are in a room with a bookshelf with scuff marks on the ground, a painting, and a book on the shelf,\n"
             "there is a strange small opening in the wall north and a open door East w")

ATTIC = Room('The Attic', 'HALLWAY', None, None, None, ["Tree House Ladder", "Iron Chestplate", "Iron Boots"],
             "there is not much here just dust, webs, and a stair case that you came from that goes north")

MASTERROOM1 = Room('Master Room 1', 'DINNINGROOM', None, None, 'HALLWAY',
                   ["Underwear", "Socks", "Shoes", "Gucci Shirt"],
                   "The room is filled with pictures of you and has posters of princesses lets hurry theres a exit \n"
                   "West and North")

MAINLIVINGROOM = Room('Main Living Room', 'KITCHEN', 'PORCH', None, None,
                      ["Shoes", "Jacket", "Socks"],
                      "Not much here just a couch, a fireplace, and a TV, oh wait oh no don't wake up vicky shes on \n"
                      "the couch asleep.")

MOM_DAD = Room("Vicky's Mom And Dads Room", None, 'HALLWAY', None, None, ["Candy", "French Fries"],
               "The room is filled with a bed, nice paintings, and a fur rug ")

HALLWAY = Room('The Main Hallway', 'MOM_DAD', 'ATTIC', 'MASTERROOM1', 'VROOM',
               ["Apple", "Big Mac"], "Some  family pictures and 4 doors")

HALLWAY1 = Room('Hallway 1', 'PLAYROOM', 'KITCHEN', None, None, ["Apple", "McChicken"],
                "Just Some family Pictures and random pictures.")

LIVINGROOM = Room('LivingRoom', 'OUTSIDE', None, 'HALLWAY2',
                  None, ["Shoes", "Track Suit", "Socks", "Gucci Shirt"], "\n"
                  "There is a couch with 4 tables a smaller 1 seat recliner, and a fireplace")

KITCHEN = Room('Kitchen', 'HALLWAY1', 'MAINLIVINGROOM', 'GARAGE', 'DINNINGROOM',
               ["Cookie", "Apple"], 'The Room Is Filled '
               'with a lovely smell')

STREET = Room('Street', None, None, 'TheEnd', 'PORCH', ["Wishing Cake", "Wishing Cake"],
              'You can see your home and you smell sweet sweet victory')

PORCH = Room('Porch', 'MAINLIVINGROOM', None, 'STREET', None, ["Apple", "Apple"],
             'You have Done it your outside and there is one other path other than where you came from')

TheEnd = Room('TheEnd', None, None, None, 'STREET', ["Trophy", "Tier III Boots"], 'Congratulations you one the game')

GARAGE = Room('Garage', None, None, None, 'KITCHEN', ["Key", "Tree House Ladder"],
              'Filled with dust and cobwebs with a shelf,'
              'ladder, and it looks like a key on the shelf')

SECRETROOM = Room('Secret Room', None, 'VROOM', None, None, ["Wishing Cake", "Excalibur"],
                  'The room is completely blue')

GARDEN = Room('Garden', None, 'TREEHOUSE', None, None, ["Apple", "Carrot"], 'It is filled with no life with a box '
              'saying Bucky on it with a hole next to it')

OUTSIDE = Room('Outside', None, 'LIVINGROOM', 'TREEHOUSE', None, ["Pick Axe", "Shoes"], 'Looks kinda dead, but it has'
               ' a small playground')

TREEHOUSE = Room('Tree house', 'GARDEN', None, None, 'OUTSIDE',
                 ["Key", "Tier III Chestplate", "Tier III Leggings", "Tier III Helmet", "Tier III Boots", "Excalibur"],
                 "A Room That seems to be small, but looks can be deceiving and its filled with amazing Items.")

HALLWAY2 = Room('Hallway 2', None, None, 'PLAYROOM', 'LIVINGROOM', ["Apple", "French Fries"],
                "A big wide Hallway That is filled with Pictures ")

DINNINGROOM = Room('Dinning Room', None, 'MASTERROOM', 'KITCHEN', None, ["Apple", "Big Mac"],
                   'WIth a long table with some fruit ,and 20 chairs and some toys on the ground')

PLAYROOM = Room('Play Room', None, 'HALLWAY1', None, 'HALLWAY2', ["wood Sword", "Apple", "Shoes", "Gucci Shirt"],
                'Filled with a ball pit, wood sword, An Apple, some Shoes, and a Gucci Shirt')

Vickys_current_node = LIVINGROOM
current_node = VROOM
directions = ['north', 'south', 'west', 'east']
short_directions = ['n', 's', 'w', 'e']

while True:

    print(current_node.name)
    print()
    print(current_node.description)
    print()
    print("Your heath is at")
    print(Timmy.health)
    print()
    print(Timmy.money)
    print()
    print(Timmy.inventory)
    print()
    print("\n".join(current_node.items))
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    if command == 'die':
        print("Your Dead")
        quit(0)
    if command == 'eat':
        print("you eat Something")
        trash = input('What Do you want to eat').lower()
        Timmy.health = 100 + 10
        Timmy.inventory.remove(trash)
    if command == 'Drop':
        print("You have thrown out a item")
        dropping = input('what item do you want to throw out.').lower()
        Timmy.inventory.remove(dropping)
    if command == 'sell':
        print("You made money")
        Selling = input('What do you want to sell')
        money = Timmy.money + input()

    elif command == 'take':
        found = False
        if len(current_node.items) > 0:
            for items in current_node.items:
                print(items)
        CMD = input('What Item?').lower()
        for items in current_node.items:
            if CMD == items.lower():
                Timmy.inventory.append(CMD)
                current_node.items.remove(items)
                found = True
                print("The items in your inventory")

    elif 'take' in command:
        item_requested = command[5:]
        for items in current_node.items:
            if items.name == item_requested:
                Timmy.inventory(current_node.items)

    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")
    else:
        print('Command not Recognized')

    if current_node.name == 'TheEnd':
        print("You Win")
        print("       x       ")
        print("x    + + +    x")
        print("  + + + + + +  ")
        print(" + + + + + + + ")
        print("  + + + + + +  ")
        print("x    + + +    x")
        print("       x       ")
        print("Good Game Good Game Could Have Been Better ,But Deal With It.")
        quit(0)

    if current_node == PORCH:
        if command in ["south", "s"]:
            if 'Key' in Timmy.inventory:
                print("You opened the door you may now pass")
            else:
                print("You can not pass")
