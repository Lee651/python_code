import json 
import pygal 
import math 
from itertools import groupby 

filename = "btc_close_2017.json"
with open(filename) as f:
    btc_data = json.load(f)


with open("收盘价Dashboard.html", "w", encoding="utf8") as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><metacharset="utf-8"></head><body>\n')
    for svg in ["收盘价折线图 .svg", "收盘价对数变化折线图 .svg", "收盘价月日均值 .svg", "收盘价周日均值 .svg", "收盘价星期均值 .svg"]:
        html_file.write('  <object type="image/svg+xml" data="{0}" height=500></object>\n' .format(svg))

    html_file.write("</body></html>")
