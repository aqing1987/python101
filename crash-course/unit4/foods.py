my_foods = ['pizza', 'falafel', 'carrot cake']

# friend_foods points to the same list same as my_foods
# friend_foods = my_foods

# create a new list and copy my_foods list items to it
friend_foods = my_foods[:]

my_foods.append("cannoli")
print('My favorite foods are:')
print(my_foods)

friend_foods.append("ice cream")
print("\nMy friend's favorite foods are:")
print(friend_foods)
for food in friend_foods:
    print(food)
