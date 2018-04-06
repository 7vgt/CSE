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

    def past_story(self):
        print("They are an employed at Krispy Cream Donunts and did not make good life choices in there past.")


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


My_Character = Characters('Timmy', None, 'Sword, Blocks, Healing Potion', 'Speed, Jump Boost, weakness', 100, 'Normal',
                          '4ft 9in, 92P', 'He is kinda short with, blue eyes, buck teeth, And always wearing a pink hat', None, None)

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

VROOM = Room('Vickys room', 'SECRETROOM', None, 'HALLWAY', None, None,
             "you are in a room with a bookshelf with scuff marks on the ground, a painting, and a book on the shelf,\n"
             "there is a strange small opening in the wall north and a open door East w")

ATTIC = Room('The Attic', 'HALLWAY', None, None, None, None,
             "theres not much here just dust, webs, and a stair case that you came from that goes north")

MASTERROOM1 = Room('Master Room 1', 'LIVINGROOM', None, None, 'HALLWAY', None,
                   "The room is filled with pictures of you and has posters of princesses lets hurry theres a exit \n"
                   "West and North")

MAINLIVINGROOM = Room('Main Living Room','KITCHEN', 'PORCH', None, None, None,
                      "Not much here just a couch, a firplace, and a TV, oh wait oh no don't wake up vicky shes on \n"
                      "the couch asleep.")

MOM_DAD = Room('Vickys Mom And Dads Room', None, 'HALLWAY', 'MASTERBATHROOM1', None, None,
               "The room is filled with a bed, nice paintings, and a fur rug ")

HALLWAY = Room('The Main Hallway', 'MASTERROOM1', 'ATTIC', 'MASTERROOM1', 'VROOM', None,
               "Some  family pictures and 4 doors")

HALLWAY1 = Room('Hallway 1', 'HALLWAY', None, None, None, None,"Just Some family Pictures and random pictures.")

LIVINGROOM = Room('LivingRoom', None, 'MASTERROOM1', 'KITCHEN', None, None, "There is a couch with 4 tables a \n"
                                                                            "smaller 1 seat recliner, and a fireplace")

KITCHEN = Room('kitchen', 'HALLWAY', 'MAINLIVINGROOM', 'GARAGE', 'LIVINGROOM', None, 'The Room Is Filled \n'
                                                                                     'with a lovly smell')

STREET = Room('Street', None, None, 'PORCH', 'YOUWIN', None, 'Room looks like your home And has a smell \n'
                                                             'of sweet sweet victory')

PORCH = Room('Porch', 'MAINLIVINGROOM', None, 'STREET', None, None, 'You have Done it your outside and theres \n'
                                                                    'one other path other than where you came from')

YOUWIN = Room('You Win', None, None, None, 'STREET', 'Trophi', 'Congradulations you one the game')

GARAGE = Room('Garage', None, None, None, 'KITCHEN', 'Key', 'Filled with dust and cobwebs with a shelf, \n'
                                                            'cobwebs, ladder, and it looks like a key on the shelf')

SECRETROOM = Room('Secret Room', None, 'VROOM', None, None, 'A Wish', 'The room is completly blue')

GARDEN = Room('Garden', None, 'TREEHOUSE', None, None, 'Carrots', 'It is filled with no life with a box \n'
                                                                  'saying beny on it with a hole next to it')

OUTSIDE = Room('Outside', None, 'LIVINGROOM', 'TREEHOUSE', None, 'Blocks, pickaxe', 'Looks kinda dead, but it has\n'
                                                                                    ' a small playground')

TREEHOUSE = Room('Tree house', None, None, None, None, None, None)

HALLWAY2 = Room('Hallway 2', None, None, None, 'DINNINGROOM', None, None)

DINNINGROOM = ('Dinning Room', None, 'MasterRoom', None, 'Kitchen', None, 'WIth a long table with some fruit,\n'
                                                                          ' 20 chairs and some toys on the ground')

#initialize rooms
vickys_roo = Room("west of house", "north_house", None, None, None, None, None)
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


