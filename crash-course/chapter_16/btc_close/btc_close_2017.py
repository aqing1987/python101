import json

# load data to list
with open('btc_close_2017.json') as f:
    btc_data = json.load(f)

# print each data
for btc_dict in btc_data:
    date = btc_dict['date']
    month = btc_dict['month']
    week = btc_dict['week']
    weekday = btc_dict['weekday']
    close = btc_dict['close']
    print("{} is month {} week {}, {}, the close price is {} RMB.".format(date, month, week, weekday, close))


