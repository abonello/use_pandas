import datetime                     # used to tell Pandas some dates that we want to pull data between.
import pandas
from pandas_datareader import data  # use this to pull data from the internet. 
# pandas_datareader was previously known as pandas.io.data
import matplotlib.pyplot as plt
from matplotlib import style

'''
The Pandas module is a high performance, highly efficient, and high level data analysis library.
'''

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

# create a dataframe
df = data.DataReader("XOM", "yahoo", start, end) # pulls data for Exxon from the Yahoo Finance API

print df.head(20)

# Plotting with Pandas

