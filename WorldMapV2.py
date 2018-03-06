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

VROOM = Room('Vickys room', 'SECRETROOM', None, 'HALLWAY', None, None,"you are in a room with a bookshelf with scuff marks on the ground, a painting, and a book on the shelf, there is a strange small opening in the wall north and a open door East w")

ATTIC = Room('The Attic', 'HALLWAY', None, None, None, None,"theres not much here just dust, webs, and a stair case that you came from that goes north")

MASTERROOM1 = Room('Master Room 1', 'LIVINGROOM', None, None, 'HALLWAY', None, "The room is filled with pictures of you and has posters of princesses lets hurry theres a exit West and North")

MAINLIVINGROOM = Room('Main Living Room','KITCHEN', 'PORCH', None, None, None,"Not much here just a couch, a firplace, and a TV, oh wait oh no don't wake up vicky shes on the couch asleep.")

MOM/DAD = Room('Vickys Mom And Dads Room', None, 'HALLWAY', 'MASTERBATHROOM1', None, None, "The room is filled with a bed, nice paintings, and a fur rug ")

HALLWAY = Room('The Main Hallway', 'MASTERROOM1', 'ATTIC', 'MASTERROOM1', 'VROOM', None, "some  family pictures and 4 doors")

HALLWAY1 = Room('Hallway 1', 'HALLWAY2', None, None, None, None,"Just Some family Pictures and random pictures.")

LIVINGROOM = Room('LivingRoom', None, 'MASTERROOM1', 'KITCHEN', None, None, "There is a couch with 4 tables a smaller 1 seat recliner, and a fireplace")

KITCHEN = Room()

STREET = Room()

PORCH = Room()

YOUWIN = Room()

GARAGE = Room()

SECRETROOM = Room()

GARDEN = Room()

OUTSIDE = Room()

TREEHOUSE = Room()

HALLWAY2 = Room('Hallway 2', None, None, None, 'DINNINGROOM', None, )

DINNINGROOM = ()

#initialize rooms
vickys_room = Room("west of house", "north_house", )
directions = ['north', 'south', 'west', 'east']
short_directions = ['n','s', 'w', 'e']

while True:
    print(current_node******)
    print(current_node******)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        #loook for which commmand we typed in
        pos = short_directions.index(command)
        #change the command to be the long form
        command = directions[pos]

    if command in directions:
        try:
            *********

