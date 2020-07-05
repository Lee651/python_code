import json 
import pygal 
import math 

filename = "btc_close_2017.json"
with open(filename) as f:
    btc_data = json.load(f)

dates = []
month = []
weeks = []
weekdays = []
close = []

for btc_dict in btc_data:
    dates.append(btc_dict["date"])
    month.append(int(btc_dict["month"]))
    weeks.append(int(btc_dict["week"]))
    weekdays.append(btc_dict["weekday"])
    close.append(float(btc_dict["close"]))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)

line_chart.title = "收盘价对数变换"
line_chart.x_labels = dates

N = 20
line_chart.x_labels_major = dates[::N]

close_log = [math.log10(x) for x in close]

line_chart.add("log收盘价", close_log)

line_chart.render_to_file("收盘价对数变化折线图.svg")