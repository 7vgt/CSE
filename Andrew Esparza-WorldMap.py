world_map = {
    'VROOM': {
        'NAME': "Vicky's room",
        'DESCRIPTION': 'you are in a room with a bookshelf with scuff marks on the ground, a painting, and a book on '
                       'the shelf, theres a locked door north and a open door East w',
        'PATHS': {
            'NORTH': 'LOCKEDDOOR',
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
    'MASTERBATHROOM2': {
        'NAME':'Master Bathroom 2',
        'DESCRIPTION':"The room is filled with pictures of you "
                      "and has posters of princesses lets hurry theres a exit West and North",
        'PATHS': {
            'NORTH': 'LIVING ROOM',
            'WEST': 'HALLWAY'
        }
    },
    'PORCH': {
        'NAME': "Porch",
        'DESCRIPTION': 'You Have Escaped Vickys House you win',
        'PATHS': {
            'NORTH': 'MAINLIVINGROOM',
            'EAST': 'Street'
        }
    },
    'MAINLIVINGROOM': {
        'NAME': 'main living room',
        'DESCRIPTION': "not much just a couch, a firplace, and a TV",
        'PATHS': {
            'NORTH': 'HALLWAY'
        }
    },
    'Mom/Dad': {
        'NAME': "vicky's mom and dads room",
        'DESCRIPTION': "The room is filled with pictures of you "
                       "and has posters of princesses lets hurry theres a exit West and North",
        'PATHS': {
            'EAST': 'MASTERBEDROOM1',
            'SOUTH': 'HALLWAY'
        }
    },
    "MASTERBATHROOM1": {
        'NAME': "Mom and Dad's bathroom",
        'DESCRIPTION': "The room is filled with pictures of you "
                       "and has posters of princesses lets hurry theres a exit West and North",
        'PATHS': {
            'WEST': 'MOMANDDADSROOM',
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
    'OUTSIDE': {
        'Name': 'OUTSIDE',
        'DESCRIPTION': 'nothing but a sand pit with a treasure chest that is empty',
        'PATHS': {
            'SOUTH': 'DINNINGROOM',
            'EAST': 'TREEHOUSE'
}
    },
    'HALLWAY': {
        'NAME': 'OUTSIDE',
        'DESCRIPTION': 'nothing but a sand pit with a treasure chest that is empty',
        'PATHS': {
            'SOUTH': 'DINNINGROOM',
            'EAST': 'TREEHOUSE'
},
    },
    'LIVINGROOM': {
        'NAME': "Vicky's room",
        'DESCRIPTION': 'you are in a room with a bookshelf with scuff marks on the ground, a painting, and a book on '
                       'the shelf, theres a locked door north and a open door East w',
        'PATHS': {
            'WEST': 'HALLWAY',
            'SOUTH': 'HALLWAY'
        }
     },
    'KITCHEN': {
        'NAME': 'Kitchen',
        'DESCRIPTION': "theres not much here just dust, webs, and a stair case that you came from that goes north",
        'PATHS': {
            'NORTH':'HALLWAY'
        }
    },
    'MASTERBATHROOM2': {
        'NAME':'MASTER BEDROOM 2',
        'DESCRIPTION':"The room is filled with pictures of you "
                      "and has posters of princesses lets hurry theres a exit West and North",
        'PATHS': {
            'NORTH': 'HALLWAY',
            'WEST': 'HALLWAY'
        }
    },
    'PORCH': {
        'NAME': "Porch",
        'DESCRIPTION': 'You Have Escaped Vickys House you win',
        'PATHS': {
            'EAST': 'Street'
        }
    },
    'Main Living Room': {
        'NAME': 'The Attic',
        'DESCRIPTION': "theres not much here just dust, webs, and a stair case that you came from that goes north",
        'PATHS': {
            'NORTH': 'HALLWAY'
        }
    },
    'Mom/Dad': {
        'NAME': 'MASTER BEDROOM 2',
        'DESCRIPTION': "The room is filled with pictures of you "
                       "and has posters of princesses lets hurry theres a exit West and North",
        'PATHS': {
            'EAST': 'MASTERBEDROOM1',
            'SOUTH': 'HALLWAY'
        }
    },
    'MASTERBATHROOM': {
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
    'HALLWAY': {
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


