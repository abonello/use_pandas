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

style.use('fivethirtyeight')

df['High'].plot()
plt.legend()
plt.show()

'''
Data prior to being loaded into a Pandas Dataframe can take multiple forms, but generally it needs 
to be a dataset that can form to rows and columns. Ex a dictionary like this:
'''
web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 34, 65, 56, 29, 76],
             'Bounce Rate': [65, 67, 78, 65, 45, 52]}

#  turn the dictionary to a dataframe 
df1 = pandas.DataFrame(web_stats)

# print first part
print df1.head(3) # dafault is 5 lines

# print end part
print df1.tail(2) # dafault is 5 lines

'''
You can see here how there are these numbers on the left, 
0,1,2,3,4,5 and so on, like line numbers. These numbers are 
actually your "index." The index of a dataframe is what the 
data is related by, ordered by etc. Generally, it is going 
to be the variable that connects all of the data. In this case, 
we never defined anything for this purpose, and it would be 
a challenge for Pandas to just somehow "know" what that 
variable was. Thus, when you do not define an index, 
Pandas will just make one for you like this.

Looking at the data set right now, do you see a column 
that connects the others?
The "Day" column fits that bill! Generally if you have
any dated data, the date will be the "index".

Once you have a reasonable index that is either a datetime 
or a number like we have, then it will work as an X axis.
'''

df1.set_index('Day', inplace=True)
# print first part
print df1.head(4) # dafault is 5 lines

# print end part
print df1.tail(4) # dafault is 5 lines

'''
Without inplace=True, the set_index would create a new object, 
which we might then put into another variable, like:

new_df = df1.set_index('Day')
'''


print df1['Visitors']
# You can also reference parts of the dataframe like an object, so long as there aren't any spaces
print df1.Visitors

df1['Visitors'].plot()
plt.legend()
plt.title('Visitors')
plt.show()


df1.plot()
plt.legend()
plt.title('All Data')
plt.show()

# We can also select more than one column to print
#print df[['Visitors','Bounce Rate']]
# So that's a list of column headers, held by brackets within brackets from the dataframe.
df[['High', 'Low', 'Open', 'Close']].plot() 
plt.legend()
plt.title('Plot Many Columns')
plt.show()