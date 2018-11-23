import numpy as np
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas_datareader.data as web
import datetime
import fix_yahoo_finance as yf

yf.pdr_override()

plt.style.use('ggplot')

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2017, 5, 1)
baba = web.get_data_yahoo('BABA', start, end)

# date = np.array(baba['Date'])
baba['Date'] = baba.index
baba.reindex(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
volume = np.array(baba['Volume'])
baba2 = []
for index, row in baba.iterrows():
    row = tuple(row)
    baba2.append(row)
date = np.array(baba['Date'])

left, width = 0.1, 0.8
rect_vol = [left, 0.1, width, 0.26]
rect_main = [left, 0.4, width, 0.5]

fig = plt.figure()

ax_vol = fig.add_axes(rect_vol)
ax_vol.fill_between(date, volume, color='y')
# ax_vol.xaxis_date()
plt.setp(ax_vol.get_xticklabels(), rotation=30, horizontalalignment='right')

ax_main = fig.add_axes(rect_main)
candlestick_ohlc(ax_main, baba2, width=0.6, colorup='r', colordown='g')

plt.show()