import json 
import pygal 
import math 
from itertools import groupby 

filename = "btc_close_2017.json"
with open(filename) as f:
    btc_data = json.load(f)

dates = []
months = []
weeks = []
weekdays = []
close = []

for btc_dict in btc_data:
    dates.append(btc_dict["date"])
    months.append(int(btc_dict["month"]))
    weeks.append(int(btc_dict["week"]))
    weekdays.append(btc_dict["weekday"])
    close.append(float(btc_dict["close"]))

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])

    x_unique, y_mean = [*zip(*xy_map)]

    line_chart = pygal.Line()

    line_chart.title = title
    line_chart.x_labels = x_unique

    line_chart.add(y_legend, y_mean)

    line_chart.render_to_file(title+ ".svg")

    return line_chart

idx_week = dates.index("2017-12-11")
line_chart_week = draw_line(weeks[: idx_week], close[: idx_week], "收盘价周日均值", "周日均值")
line_chart_week 