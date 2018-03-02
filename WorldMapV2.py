class room(object):
    def __init__(self, name, north, east, south, west, items):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.items = items

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


#initialize rooms
vickys_room = room("west of house", "north_house", )
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

