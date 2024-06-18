'''-------data analsis (eda ) practice task-------'''

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('dark_background')
sns.set_style('darkgrid')

sns.get_dataset_names()

df=pd.read_csv(r"F:/python/hr_data.csv")
print(df.head())  # Display the first five rows
print(df.shape)  # dimensions (rows, columns)

# The info() method is used in pandas to get a concise summary of a DataFrame. 
# This method is particularly including the number of non-null entries in each column, the data types of each column, and the memory usage of the DataFrame.
print(df.info())

# Univariate analysis of the 'signal' column
# Load the 'fmri' dataset
data = sns.load_dataset('fmri')
sns.histplot(data['signal'], kde=True)
plt.title('Distribution of Signal')
plt.show()

# Bivariate analysis
sns.scatterplot(data=data, x='timepoint', y='signal')
plt.title('Scatter Plot of Timepoint vs. Signal')
plt.show()


# Multivariate analysis using a scatter plot with hue and style
sns.lineplot(x = 'number_project', y = 'average_montly_hours', data = df, 
             hue = 'left',
             style = 'department',
             legend ='full',
             palette = 'flare')
plt.title('Multivariate Scatter Plot')
plt.show()
# Understanding the "hue" Parameter-->
# The hue parameter is used to add a third dimension to the plot by coloring the data points based on the categories of a given column.
# This helps in distinguishing different groups within the data.


# Load the 'flights' dataset
flights = sns.load_dataset('flights')

# Pivot the dataset to a wide-format DataFrame
flights_pivot = flights.pivot("month", "year", "passengers")
Pivot the DataFrame: The DataFrame is pivoted to have months as rows, years as columns, and the number of passengers as values.
# Creating a heatmap

# annot=True: Annotates each cell with the numeric value.
# fmt="d": Specifies that the annotations should be formatted as integers.
# cmap="YlGnBu": Uses the "Yellow-Green-Blue" color map.
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")
plt.title('Heatmap of Flight Passengers')
plt.show()


#   diff between crosstab and heatmap?
#   Functionality:

# crosstab: Focuses on creating a summary table (contingency table) to show the frequency or aggregation of categorical data.
# heatmap: Focuses on visualizing data, particularly matrix-like data, using color gradients.
# Output:

# crosstab: Produces a DataFrame.
# heatmap: Produces a graphical plot.
# Usage Context:

# crosstab: Used for data preparation and summarization.
# heatmap: Used for data visualization.

#   Relationship:
# You often use crosstab to create a summarized DataFrame and then visualize that DataFrame using heatmap.
# The crosstab function helps in structuring and aggregating the data, while the heatmap function helps in visualizing the aggregated data to easily identify patterns.
