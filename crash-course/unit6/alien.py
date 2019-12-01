alien0 = {'color': 'green', 'points': 5}
print(alien0)

print(alien0['color'])
print(alien0['points'])

new_points = alien0['points']
print("You just earned " + str(new_points) + " points!")

# add key-value
alien0['x_position'] = 0
alien0['y_position'] = 25
print(alien0)

alien1 = {}
alien1['color'] = 'red'
alien1['points'] = 8
print(alien1)

# change value in dictionary
alien0 = {'color': 'green'}
print("The alien is " + alien0['color'] + ".")

alien0['color'] = 'yellow'
print("The alien is now " + alien0['color'] + ".")

alien0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien0['x_position']))

# alien move to right
if alien0['speed'] == 'slow':
    x_increment = 1
elif alien0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# compute new position
alien0['x_position'] = alien0['x_position'] + x_increment
print("New x-position: " + str(alien0['x_position']))

# delete key-value
alien0 = {'color': 'green', 'points': 5}
print(alien0)

del alien0['points']
print(alien0)
