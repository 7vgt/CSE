world_map = {
    'WESTHOUSE': {
        'NAME': "West Of House",
        'DESCRIPTION': 'you are west of a white house',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
     },
    'NORTHHOUSE': {
        'NAME': 'North Of House',
        'DESCRIPTION': "Insert Description Here",
        'PATHS': {
            'SOUTH':'WESTHOUSE'
        }
    },
    'SOUTHHOUSE': {
        'NAME':'South of house',
        'DESCRIPTION':"Insert Description Here",
        'PATHS': {
            'NORTH':'WESTHOUSE'
        }
    }
}
