world_map = {
    'Vroom': {
        'NAME': "Vicky's room",
        'DESCRIPTION': 'you are in a room with a bookshelf with scuff marks on the ground, a painting, and a book on '
                       'the shelf, theres a locked door north and a open door East w',
        'PATHS': {
            'NORTH': 'LOCKEDDOOR',
            'EAST': 'HALLWAY'
        }
     },
    'Attic': {
        'NAME': 'The Attic',
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
    }
    'GARDEN' : {
        'NAME': 'GARDEN',
        'DESCRIPTION': 'not much theres just some carrot and tomato plants',
        'PATHS' : {
            'SOUTH' : 'Outside'
        }
    }
    'OUTSIDE' : {
        'Name' : 'OUTSIDE',
        'DESCRIPTION': 'nothing but a sand pit with a treasure chest thats empty',
        'PATHS' : {
            'SOUTH' : 'DINNINGROOM',
            'EAST' : 'TREEHOUSE'
}
    }
}
