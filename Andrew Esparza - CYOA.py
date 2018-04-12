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
    def __init__(self, name, value, Description):
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
        print("It snuggly fits you")


class Radio(Item):
    def __init__(self, name, value):
        super(Radio, self).__init__(name, value)

    def singing(self):
        print("(Song Lyrics)Just Have Mercuyyyy on my heartt...."
              "Can I take back And just star all over")


Apple = Food('Apple', '$1', 10)

Cookie = Food('Cookie', '$2.50', 2)

cheese = Food('Cheese', '$100', 20)

Wishing_cake = Food('Wishing Cupcake', '$10,000', 100)

Candy = Food('Candy', '$1', 2)

Carrot = Food('Carrot', '$4', 5)

Stone_blocks = Blocks('Stone block', '$5')

Wood_blocks = Blocks('Wood', '$5')

Gucci_shirt = Clothes('Guccis shirt', '$1000', 'Gucci')

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

Iron_Helment = Armour('Iron Helment', '$40', 'Iron')

Iron_Chestplate = Armour('Iron Chestplate', '$80', 'Iron')

Iron_leggings = Armour('Iron Leggings', '$60', 'Iron')

Iron_Boots = Armour('Iron Boots', '$40', 'Iron')

Diamond_Helment = Armour('Diamond Boots', '$1000', 'Diamond')

Diamond_Chestplate = Armour('Tier III ChestPlate', '$1400', 'Diamond')

Diamond_Leggings = Armour('Tier III leggings', '$1200', 'Diamond')

Diamond_Boots = Armour('Tier III Boots', '$1000', 'Diamond')

Wood_sword = Weapon('Tier III Sword', '$20')

stone_sword = Weapon('Stone Sword', '$40')

Gold_sword = Weapon('Gold Sword', '$120')

Steel_Sword = Weapon('Steel Sword', '$60')

Diamond_sword = Weapon('Excalibur', '$1000')

Pick_Axe = Tool('Pick Axe','$250')

Legendary_Axe_Of_Amazing_Fantasticnes = Tool('Axe', '$500')

Code_Breaker = Tool('Axe', '$1000000')

TreeHouse_Ladder = Ladder('Tree House Ladder', None)


class Characters(object):
    def __init__(self, name, move, inventory, abilities, health, status, physique, description, take_damage,
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


You = Characters('Timmy', None, 'Sword, Blocks, Healing Potion', 'Speed, Jump Boost, weakness', 100, 'Normal',
                          '4ft 9in, 92P', 'He is kinda short with, blue eyes, buck teeth, And always wearing a pink hat', None, None)

Vicky = Characters('Vicky', None, None, 'Speed', 1000, 'Speed', '5ft 9Inches', 'She has orange \n'
                    'hair with a burning look of anger that will frighten anyone', None, None)

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

VROOM = Room('Vickys room', 'SECRETROOM', None, 'HALLWAY', None, Key,
             "you are in a room with a bookshelf with scuff marks on the ground, a painting, and a book on the shelf,\n"
             "there is a strange small opening in the wall north and a open door East w")

ATTIC = Room('The Attic', 'HALLWAY', None, None, None, Ladder,
             "theres not much here just dust, webs, and a stair case that you came from that goes north")

MASTERROOM1 = Room('Master Room 1', 'LIVINGROOM', None, None, 'HALLWAY\n'
                   , [Calvan_Kalin_Underwear, Supreme_socks, Yeezys_Shoes, Gucci_shirt],
                   "The room is filled with pictures of you and has posters of princesses lets hurry theres a exit \n"
                   "West and North")

MAINLIVINGROOM = Room('Main Living Room','KITCHEN', 'PORCH', None, None, Yeezys_Shoes,
                      "Not much here just a couch, a firplace, and a TV, oh wait oh no don't wake up vicky shes on \n"
                      "the couch asleep.")

MOM_DAD = Room('Vickys Mom And Dads Room', None, 'HALLWAY', 'MASTERBATHROOM1', None, Candy,
               "The room is filled with a bed, nice paintings, and a fur rug ")

HALLWAY = Room('The Main Hallway', 'MOM_DAD', 'ATTIC', 'MASTERROOM1', 'VROOM', None,
               "Some  family pictures and 4 doors")

HALLWAY1 = Room('Hallway 1', 'HALLWAY2', 'KITCHEN', None, None, None,"Just Some family Pictures and random pictures.")

LIVINGROOM = Room('LivingRoom', None, 'MASTERROOM1', 'KITCHEN\n'
                 , None, [Yeezys_Shoes, Addidas_Shoes,Supreme_socks, Gucci_shirt], "\n"
                  "There is a couch with 4 tables a smaller 1 seat recliner, and a fireplace")

KITCHEN = Room('Kitchen', 'HALLWAY1', 'MAINLIVINGROOM', 'GARAGE', 'LIVINGROOM', [Cookie, Apple], 'The Room Is Filled \n'
                                                                                     'with a lovly smell')

STREET = Room('Street', None, None, 'YOUWIN', 'PORCH', None, 'Room looks like your home And has a smell \n'
                                                             'of sweet sweet victory')

PORCH = Room('Porch', 'MAINLIVINGROOM', None, 'STREET', None, None, 'You have Done it your outside and theres \n'
                                                                    'one other path other than where you came from')

YOUWIN = Room('You Win', None, None, None, 'STREET', 'Trophi', 'Congradulations you one the game')

GARAGE = Room('Garage', None, None, None, 'KITCHEN', [Key, Ladder], 'Filled with dust and cobwebs with a shelf, \n'
                                                            'cobwebs, ladder, and it looks like a key on the shelf')

SECRETROOM = Room('Secret Room', None, 'VROOM', None, None, Wishing_cake, 'The room is completly blue')

GARDEN = Room('Garden', None, 'TREEHOUSE', None, None, [Apple, Carrot], 'It is filled with no life with a box \n'
                                                                  'saying beny on it with a hole next to it')

OUTSIDE = Room('Outside', None, 'DINNINGROOM', 'TREEHOUSE', None, Pick_Axe, 'Looks kinda dead, but it has\n'
                                                                                    ' a small playground')

TREEHOUSE = Room('Tree house', None, None, None, None,
                 [Key, Diamond_Chestplate, Diamond_Leggings, Diamond_Helment, Diamond_Boots, Diamond_sword],
                 None)

HALLWAY2 = Room('Hallway 2', None, None, None, 'DINNINGROOM', None, None)

DINNINGROOM = ('Dinning Room', None, 'MasterRoom', None, 'Kitchen', [Apple, Legendary_Axe_Of_Amazing_Fantasticnes],
               'WIth a long table with some fruit ,and 20 chairs and some toys on the ground')

vickys_room = Room("west of house", "north_house", None, None, None, None, None)
current_node = VROOM
directions = ['north', 'south', 'west', 'east']
short_directions = ['n','s', 'w', 'e']

while True:
    print(current_node)
    print(current_node)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
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
    print()
