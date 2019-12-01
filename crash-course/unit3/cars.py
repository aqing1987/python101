cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

# permanent modification
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# will not change
print('original list')
print(cars)
print('\nhere is the sorted list')
print(sorted(cars))
print('\nHere is the original again')
print(cars)

# reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

print(len(cars))
