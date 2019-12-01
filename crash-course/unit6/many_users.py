users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    fullname = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + fullname.title())
    print("\tLocation: " + location.title())
