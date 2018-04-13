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

VROOM = Room('Vickys room', 'SECRETROOM', None, 'HALLWAY', None, "Key",
             "you are in a room with a bookshelf with scuff marks on the ground, a painting, and a book on the shelf,\n"
             "there is a strange small opening in the wall north and a open door East w")

ATTIC = Room('The Attic', 'HALLWAY', None, None, None, "Ladder",
             "theres not much here just dust, webs, and a stair case that you came from that goes north")

MASTERROOM1 = Room('Master Room 1', 'LIVINGROOM', None, None, 'HALLWAY\n'
                   , "[Calvan_Kalin_Underwear, Supreme_socks, Yeezys_Shoes, Gucci_shirt]",
                   "The room is filled with pictures of you and has posters of princesses lets hurry theres a exit \n"
                   "West and North")

MAINLIVINGROOM = Room('Main Living Room','KITCHEN', 'PORCH', None, None, "Yeezys_Shoes",
                      "Not much here just a couch, a firplace, and a TV, oh wait oh no don't wake up vicky shes on \n"
                      "the couch asleep.")

MOM_DAD = Room('Vickys Mom And Dads Room', None, 'HALLWAY', 'MASTERBATHROOM1', None, "Candy",
               "The room is filled with a bed, nice paintings, and a fur rug ")

HALLWAY = Room('The Main Hallway', 'MOM_DAD', 'ATTIC', 'MASTERROOM1', 'VROOM', None,
               "Some  family pictures and 4 doors")

HALLWAY1 = Room('Hallway 1', 'HALLWAY2', 'KITCHEN', None, None, None,"Just Some family Pictures and random pictures.")

LIVINGROOM = Room('LivingRoom', None, 'MASTERROOM1', 'KITCHEN\n'
                 , None, "[Yeezys_Shoes, Addidas_Shoes,Supreme_socks, Gucci_shirt]", "\n"
                  "There is a couch with 4 tables a smaller 1 seat recliner, and a fireplace")

KITCHEN = Room('Kitchen', 'HALLWAY1', 'MAINLIVINGROOM', 'GARAGE', 'LIVINGROOM', "[Cookie, Apple]", 'The Room Is Filled \n'
                                                                                     'with a lovly smell')

STREET = Room('Street', None, None, 'YOUWIN', 'PORCH', None, 'Room looks like your home And has a smell \n'
                                                             'of sweet sweet victory')

PORCH = Room('Porch', 'MAINLIVINGROOM', None, 'STREET', None, None, 'You have Done it your outside and theres \n'
                                                                    'one other path other than where you came from')

YOUWIN = Room('You Win', None, None, None, 'STREET', 'Trophi', 'Congradulations you one the game')

GARAGE = Room('Garage', None, None, None, 'KITCHEN', "[Key, Ladder]", 'Filled with dust and cobwebs with a shelf, \n'
                                                            'cobwebs, ladder, and it looks like a key on the shelf')

SECRETROOM = Room('Secret Room', None, 'VROOM', None, None, "Wishing_cake", 'The room is completly blue')

GARDEN = Room('Garden', None, 'TREEHOUSE', None, None, "[Apple, Carrot]", 'It is filled with no life with a box \n'
                                                                  'saying beny on it with a hole next to it')

OUTSIDE = Room('Outside', None, 'DINNINGROOM', 'TREEHOUSE', None, "Pick_Axe", 'Looks kinda dead, but it has\n'
                                                                                    ' a small playground')

TREEHOUSE = Room('Tree house', None, None, None, None,
                 "[Key, Diamond_Chestplate, Diamond_Leggings, Diamond_Helment, Diamond_Boots, Diamond_sword]",
                 None)

HALLWAY2 = Room('Hallway 2', None, None, None, 'DINNINGROOM', None, None)

DINNINGROOM = ('Dinning Room', None, 'MasterRoom', None, 'Kitchen', "[Apple, Legendary_Axe_Of_Amazing_Fantasticnes]",
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
