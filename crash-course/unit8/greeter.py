def greet_user():
    """show simple greeting"""
    print("Hello!")


def greet_user2(username):
    """show simple greeting2"""
    print("Hello, " + username.title() + "!")


greet_user()
greet_user2('jesse')


def get_formatted_name(first_name, last_name):
    """return tidy name"""
    full_name = first_name + ' ' + last_name
    return full_name


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    fname = input("first name: ")
    if fname == 'q':
        break

    lname = input("last name: ")
    if lname == 'q':
        break

    full = get_formatted_name(fname, lname)
    print("\nHello, " + full + "!")
