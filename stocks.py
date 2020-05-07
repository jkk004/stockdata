import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

plt.style.use('ggplot')
fig = plt.figure(figsize = [20,9])
print("Pick a starting year: ")
first = input()
print("Pick an ending year: ")
second = input()
print("Choose a stock (symbol not full name)")
s1 = input()
print("Choose another stock (symbol not full name)")
s2 = input()
style.use("ggplot")
start = dt.datetime(int(first),1,1)
end = dt.datetime(int(second),12,30)

df = web.DataReader(s1, 'yahoo', start,end)
df["Adj Close"].plot(label=s1.upper())
df1 = web.DataReader(s2, 'yahoo', start,end)
df1["Adj Close"].plot(label=s2.upper())
df2 = (df1["Adj Close"] + df["Adj Close"])/2
df2.plot(label = "Average")
plt.legend()
plt.title(s1.upper() + " VS " + s2.upper())

plt.show()
