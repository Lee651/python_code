import csv

from datetime import datetime 

from matplotlib import pyplot as plt 

filename = "sitka_weather_2014.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
            
        except ValueError:
            print(current_date, "missing data")

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(8,5))

plt.plot(dates, highs, c="red", alpha=0.5, linewidth=1)
plt.plot(dates, lows, c="blue", alpha=0.5, linewidth=1)
plt.fill_between(dates, highs, lows, facecolor="green", alpha=0.1)

plt.title("Daily high/low tempeture of 2014", fontsize=20)
plt.xlabel(" ", fontsize=15)
plt.ylabel("Tempeture", fontsize=15)
fig.autofmt_xdate()

plt.tick_params(axis="both", which= "major", labelsize=10)

plt.show()

