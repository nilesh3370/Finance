import datetime as d
import matplotlib.pyplot 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = d.datetime(2017,1,1)
end = d.datetime(2017,2,2)

df = web.DataReader('tsla','google', start, end)
df.to_csv('tsla.csv')
df =pd.read_csv('tsla.csv',parse_dates = True,index_col = 0)
print(df.head())
df.plot()
matplotlib.pyplot.show()
