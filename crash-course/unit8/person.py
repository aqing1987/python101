def build_person(first_name, last_name, age=''):
    """return a dictionary, including one person's infomation"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
