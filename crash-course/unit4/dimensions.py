dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# tuple object does not support item assignment
# dimensions[0] = 250

for dimension in dimensions:
    print(dimension)

# can change tuple variable
menus = ('rice', 'noodles', 'dumplings')
for menu in menus:
    print(menu)

menus = ('rice', 'beef', 'pork')
for menu in menus:
    print(menu)
