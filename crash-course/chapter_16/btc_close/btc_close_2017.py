import json
import pygal
import math

# load data to list
with open('btc_close_2017.json') as f:
    btc_data = json.load(f)

dates = []
months = []
weeks = []
weekdays = []
close = []
# each day's info
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
    #print("{} is month {} week {}, {}, the close price is {} RMB.".format(date, month, week, weekday, close))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = "收盘价"
line_chart.x_labels = dates
N = 20 # x坐标轴每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('收盘价', close_log)
line_chart.render_to_file('close_log.svg')
