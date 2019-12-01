alien0 = {'color': 'green', 'points': 5}
alien1 = {'color': 'yellow', 'points': 10}
alien2 = {'color': 'red', 'points': 15}

aliens = [alien0, alien1, alien2]

for alien in aliens:
    print(alien)

print("\n 2nd")

aliens = []

# create 30 green aliens
for alien_number in range(30):
    new_align = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_align)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))
