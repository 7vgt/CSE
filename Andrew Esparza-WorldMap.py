world_map = {
    'VROOM': {
        'NAME': "Vicky's room",
        'DESCRIPTION': 'you are in a room with a bookshelf with scuff marks on the ground, a painting, and a book on '
                       'the shelf, there is a strange small opening in the wall north and a open door East w',
        'PATHS': {
            'NORTH': 'SECRETROOM',
            'EAST': 'HALLWAY'
        }
     },
    'ATTIC': {
        'NAME': 'The Attic',
        'DESCRIPTION': "theres not much here just dust, webs, and a stair case that you came from that goes north",
        'PATHS': {
            'NORTH':'HALLWAY'
        }
    },
    'MASTERBATHROOM1': {
        'NAME':'Master Bathroom 2',
        'DESCRIPTION':"The room is filled with pictures of you "
                      "and has posters of princesses lets hurry theres a exit West and North",
        'PATHS': {
            'NORTH': 'LIVING ROOM',
            'WEST': 'HALLWAY'

        }
    },
    'MAINLIVINGROOM': {
        'NAME': 'main living room',
        'DESCRIPTION': "Not much here just a couch, a firplace, and a TV, oh wait oh no don't wake up vicky shes on the couch asleep.",
        'PATHS': {
            'NORTH': 'KITCHEN',
            'SOUTH':'PORCH'
        }
    },
    'Mom/Dad': {
        'NAME': "vicky's mom and dads room",
        'DESCRIPTION': "The room is filled with a bed, nice paintings, and a fur rug ",
        'PATHS': {
            'EAST': 'MASTERBEDROOM1',
            'SOUTH': 'HALLWAY'
        }
    },
    'HALLWAY' : {
        'NAME': 'Main Hallway',
        'DESCRIPTION': 'some pictures and 4 doors',
        'PATHS' : {
            'SOUTH' : 'ATTIC',
            'NORTH': 'MOM AND DADS ROOM',
            'WEST': 'VROOM',
            'EAST': 'MAINBATHROOM2'
        }
    },
    'HALLWAY1': {
        'NAME': 'OUTSIDE',
        'DESCRIPTION': 'just a open hallway with family pictures',
        'PATHS': {
            'SOUTH':'KITCHEN',
            'NORTH':'HALLWAY2'
        },
    },
    'LIVINGROOM': {
        'NAME': "Living Room",
        'DESCRIPTION': 'There is a couch with 4 tables a smaller 1 seat recliner, and a fireplace',
        'PATHS': {
            'EAST': 'KITCHEN',
            'SOUTH': 'HALLWAY'
        }
    },
    'KITCHEN': {
        'NAME': 'Kitchen',
        'DESCRIPTION': "The kitchen is filled to the brim with food a fridge and a couple fresh pies on the counters.",
        'PATHS': {
            'NORTH':'HALLWAY',
            'SOUTH':'MAINLIVINGROOM',
            'WEST':'LIVINGROOM',
            'EAST':'GARAGE'
        }
    },
    'STREET': {
        'NAME':'MASTER BEDROOM 2',
        'DESCRIPTION':"The room is filled with pictures of you "
                      "and has posters of princesses lets hurry theres a exit West and North",
        'PATHS': {
            'EAST': 'YOUWIN',
            'WEST': 'PORCH'
        }
    },
    'PORCH': {
        'NAME': "Porch",
        'DESCRIPTION': 'You Have Escaped Vickys House you win',
        'PATHS': {
            'EAST': 'Street',
            'NORTH':'MAINLIVINGROOM'
        }
    },
    'YOUWIN': {
        'NAME': 'The Attic',
        'DESCRIPTION': "theres not much here just dust, webs, and a stair case that you came from that goes north",
        'PATHS': {
            'WEST': 'STREET'
        }
    },
    'GARAGE': {
        'NAME': 'MASTER BEDROOM 2',
        'DESCRIPTION': "The room is filled with pictures of you "
                       "and has posters of princesses lets hurry theres a exit West and North",
        'PATHS': {
            'WEST': 'KITCHEN'
        }
    },
    'SECRETROOM': {
        'NAME': 'MASTER BEDROOM 2',
        'DESCRIPTION': "The room is filled with pictures of you "
                       "and has posters of princesses lets hurry theres a exit West and North",
        'PATHS': {
            'WEST': 'MOMANDDADSROOM',
        }
    },
    'GARDEN' : {
        'NAME': 'GARDEN',
        'DESCRIPTION': 'not much theres just some carrot and tomato plants',
        'PATHS' : {
            'SOUTH' : 'Outside'
        }
    },
    'OUTSIDE': {
        'Name': 'OUTSIDE',
        'DESCRIPTION': 'nothing but a sand pit with a treasure chest that is empty',
        'PATHS': {
            'SOUTH': 'DINNINGROOM',
            'EAST': 'TREEHOUSE'
        }
    },
    'TREEHOUSE': {
        'NAME': 'OUTSIDE',
        'DESCRIPTION': 'nothing but a sand pit with a treasure chest that is empty',
        'PATHS': {
            'SOUTH': 'DINNINGROOM',
            'EAST': 'TREEHOUSE'
        },
    }
}



current_node = world_map['VROOM']
directions = ['SOUTH', 'NORTH','WEST','EAST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("you cannot go this way")
    else:
        print('command not recognized')


