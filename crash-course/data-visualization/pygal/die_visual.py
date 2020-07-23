import pygal

from die import Die

# create D6
D6 = Die()

# roll the die and save the results
results = []
for roll_num in range(1000):
    result = D6.roll()
    results.append(result)

# print(results)
# analysis Results
frequencies = []
for value in range(1, D6.num_sides):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# show the frequencies
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_label = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
