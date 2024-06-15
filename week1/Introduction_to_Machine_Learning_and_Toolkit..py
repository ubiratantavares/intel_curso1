import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

step_data = [3620, 7891, 9761, 3907, 4338, 5373]

step_counts = pd.Series(step_data, name='steps')

print(step_counts)

step_counts.index = pd.date_range('20150329', periods=len(step_data))

print(step_counts)

# just like a dictionary
print(step_counts['2015-04-01'])

# or by index position--like an array
# print(step_counts[3])

# select all of April
print(step_counts['2015-04'])

# view the data type
print(step_counts.dtypes)

# convert to a float
step_counts = step_counts.astype(dtype=float)

# view the data type
print(step_counts.dtypes)

# create invalid data
step_counts.iloc[1:3] = np.NaN

print(step_counts.iloc[1:3])

# now fill it in with zeros
# step_counts = step_counts.fillna(0.)
# equivalently
step_counts.fillna(0., inplace=True)

print(step_counts.iloc[1:3])

# cycling distance
cycling_data = [10.7, 0, None, 2.4, 15.3, 10.9, 0, None]

# create a tuple of data
joined_data = list(zip(step_data, cycling_data))

# the dataframe
# add column names to dataframe
activity_df = pd.DataFrame(joined_data, 
                           index=pd.date_range('20150329', 
                           periods=len(step_data)), 
                           columns=['Walking', 'Cycling'])

print(activity_df)

# select row of data by index name
print(activity_df.loc['2015-04-01'])

# select row of data by integer position
print(activity_df.iloc[-3])

# name of column
print(activity_df['Walking'])

# object-oriented approach
print(activity_df.Walking)

# first column
print(activity_df.iloc[:,0])


data_path = ['week1/data']

# the location of the data file
filepath = os.sep.join(data_path + ['Iris_Data.csv'])

print(filepath)

# import the data
data = pd.read_csv(filepath)

# print a few rows
print(data.iloc[:5])

# create a new column that is an product 
# of both measurements
data['sepal_area'] = data.sepal_length * data.sepal_width

# print a few rows and columns
print(data.iloc[:5, -3:])

# the lambda function applies what
# follows it to each row of data
data['abbrev'] = (data
                  .species
                  .apply(lambda x: x.replace('Iris-', '')))

# note that there are other ways to
# accomplish the above
print(data.iloc[:5, -3:])

# concatenate the first two and last two rows
small_data = pd.concat([data.iloc[:2], data.iloc[-2:]])

print(small_data.iloc[:, -3:])

# Aggregated Statistics with GroupBy
# Using the groupby method calculated aggregated DataFrame statistics.
# use the size method with a DataFrame to get count
# for a Series, use the .value_counts method
group_sizes = (data
               .groupby('species')
               .size())

print(group_sizes)

# Performing Statistical Calculations

# Pandas contains a variety of statistical methods—mean, median, and mode

# mean calculated on a Series
print(data.petal_length.mean())

# median calculated on a Series
print(data.petal_length.median())

# mode calculated on a Series
print(data.petal_length.mode())

# Standard deviation, variance, SEM and quantiles can also be calculated
print(data.petal_length.std(), data.petal_length.var(), data.petal_length.sem())

# as well as quantiles
print(data.petal_length.quantile(0.5))

# Multiple calculations can be presented in a DataFrame
print(data.describe())

# Sampling from DataFrames

# DataFrames can be randomly sampled from

# sample 5 rows without replacement
sample = (data
          .sample(n = 5, replace=False, random_state=42))

print(sample.iloc[:, -3:])

# note: SciPy and NumPy also contain a variety of statistical functions.

# Basic Scatter Plots
plt.plot(data.sepal_length, data.sepal_width, ls='', marker='o', label='sepal')
plt.plot(data.petal_length, data.petal_width, ls='', marker='o', label='petal')
plt.grid()
plt.xlabel('length')
plt.ylabel('width')
plt.legend()
plt.show()

# Histograms
plt.hist(data.sepal_length, bins=25)
plt.grid()
plt.show()

# customizing matplotlib plots
fig, ax = plt.subplots()

ax.barh(np.arange(10), data.sepal_width.iloc[:10])

# set position of ticks and tick labels
ax.set_yticks(np.arange(0.4, 10.4, 1.0))
ax.set_yticklabels(np.arange(1, 11))
ax.set(xlabel='xlabel', ylabel='ylabel', title='title')
plt.show()

# Statistical Plotting with Seaborn

# Joint distribution and scatter plots can be created
sns.jointplot(x='sepal_length', y='sepal_width', data=data, size=4)
plt.grid()
plt.show()

# Correlation plots of all variable pairs can also be made with Seaborn
sns.pairplot(data, hue='species', height=3)
plt.show()

