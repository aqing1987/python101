def build_profile(first, last, **user_info):
    """create a dictionary, including all the info user created"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princetion',
                             field='physics')
print(user_profile)
