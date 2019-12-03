with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    # when read() reach the end of file, return a null string
    print(contents)
