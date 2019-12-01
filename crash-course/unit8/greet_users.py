def greet_users(names):
    """send greeting to each list item"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'rama', 'tushar']
greet_users(usernames)
