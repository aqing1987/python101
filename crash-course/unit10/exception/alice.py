filename = 'alice1.txt'  # not exist

with open(filename) as f_obj:
    contents = f_obj.read()
