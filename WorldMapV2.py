class Room(object):
    def __init__(self, name, north, east, south, west, items, description):
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

Vroom = Room('Vickys room', 'SECRETROOM', None, 'HALLWAY', None, None,"you are in a room with a bookshelf with scuff marks on the ground, a painting, and a book on the shelf, there is a strange small opening in the wall north and a open door East w")

Attic = Room('The Attic', 'HALLWAY', None, None, None, None,"theres not much here just dust, webs, and a stair case that you came from that goes north")

MasterRoom1 = Room('Master Room 1', 'LIVINGROOM', None, None, 'HALLWAY', None, "The room is filled with pictures of you and has posters of princesses lets hurry theres a exit West and North")

MainLivingRoom = Room('Main Living Room','KITCHEN', 'PORCH', None, None, None,"Not much here just a couch, a firplace, and a TV, oh wait oh no don't wake up vicky shes on the couch asleep.")

MOM/DAD = Room()


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

