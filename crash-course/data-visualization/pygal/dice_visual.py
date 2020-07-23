import pygal

from die import Die

# create two D6 die
die_1 = Die()
die_2 = Die()

# roll many times, and save the results
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analysis Results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# show the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_label = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
