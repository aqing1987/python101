import csv
from datetime import datetime

from matplotlib import pyplot as plt

#filename = 'sitka_weather_07-2014.csv'
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    """
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    """
    # extract datetime and max temperature
    dates, highs = [], []
    for row in reader:
        # 0 datetime
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        # 1 Max TemperatureF
        high = int(row[1])
        highs.append(high)
    #print(highs)

# draw according to data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# set figure format
plt.title("Daily high temperature, 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
