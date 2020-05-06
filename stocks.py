import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use("ggplot")
start = dt.datetime(2020,1,1)
end = dt.datetime(2020,5,1)

df = web.DataReader('aapl', 'yahoo', start,end)
df["Adj Close"].plot(label='AAPL')
df1 = web.DataReader('msft', 'yahoo', start,end)
df1["Adj Close"].plot(label="MSFT")
df2 = (df1["Adj Close"] + df["Adj Close"])/2
df2.plot(label = "Average")
plt.legend()
plt.title("TSLA VS MSFT")
plt.show()



#df_ohlc = df['Adj Close'].resample('10D').ohlc()
#df_volume = df['Volume'].resample('10D').sum()
#df_ohlc.reset_index(inplace = True)
#df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

#mpf(ax1,df_ohlc.values, width = 2)
#ax2.fill_between(df_volume.index.map(mdates.date2num,df_volume.values,0))
#mpf.plot(df_ohlc,type='candle')