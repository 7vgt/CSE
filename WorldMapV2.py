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
vickys_room = room("west of house", "north_house", None)
