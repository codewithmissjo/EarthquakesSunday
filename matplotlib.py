import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

url = "eq-2024-v1.csv"
#url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2024-01-01&endtime=2025-01-01&orderby=magnitude&limit=100"
df = pd.read_csv(url, sep="|")

def countOfEqByM():
    # how many earthquakes happened in each month of 2024?
    months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for index, item in df.iterrows():
        # 2024-06-28T05:36:36.902
        m = int(item["Time"][5:7]) - 1
        print(m)
        months[m] += 1

    print(months)

def avgMagOfEqByM():
    # what is the average magnitude of all earthquakes in each month?
    months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    mags = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for index, item in df.iterrows():
        # 2024-06-28T05:36:36.902
        m = int(item["Time"][5:7]) - 1
        months[m] += 1
        mags[m] += item["Magnitude"]
    avg = []
    for mm in range(len(months)):
        avg.append(mags[mm] / months[mm])
    print(avg)
avgMagOfEqByM()
# bar chart
# time x axis, group by month
# magnitude y axis, chart AVG mag

# scatter plot
# x, month and day
# 2024-06-28T05:36:36.902
# y, magnitude

def forLater():
    plt.style.use('_mpl-gallery')

    # make the data
    x =[]
    y = []
    for index, item in df.iterrows():
        # 2024-06-28T05:36:36.902
        x.append(f'{item["Time"][5:7]}-{item["Time"][8:10]}')
        y.append(item["Magnitude"])

    # plot
    fig, ax = plt.subplots()

    ax.scatter(x, y, vmin=0, vmax=100)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()


'''
HW: Use the earthquake API docs to formulate your own earthquake query. then write a sentence/phrase describing the set of data you have collected. Docs here: https://earthquake.usgs.gov/fdsnws/event/1/
'''