motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.append('lastmm')
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.insert(0, 'kku')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print(motorcycles)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles.remove('suzuki')
print(motorcycles)
