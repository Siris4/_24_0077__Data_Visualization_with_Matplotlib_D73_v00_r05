import pandas as pd
import os
import matplotlib.pyplot as plt

# Change the working directory
os.chdir('C:\\Users\\Siris\\Desktop\\GitHub Projects 100 Days NewB\\_24_0077__Day73_Data_Visualization_with_Matplotlib__240812\\NewProject\\r00-r09 START\\r00_env_START')

# Load the CSV file into a DataFrame
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

# Verify the changes
print(df.shape)
print(df.head())

# Convert 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Pivot the DataFrame with monthly data
pivoted_df = df.pivot(index='DATE', columns='TAG', values='POSTS')

# Plot the 'java' tag data
plt.figure(figsize=(16, 10))
plt.plot(pivoted_df.index, pivoted_df['java'])

# Format the x-axis to show only years as labels
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y'))

# Set the x-axis ticks to show every 12 months (1 year)
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.YearLocator())

# Rotate x-axis labels for better readability and set fontsize
plt.xticks(rotation=45, fontsize=14)

# Set y-axis ticks fontsize
plt.yticks(fontsize=14)

plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)

plt.ylim(0, 35000)

# Adjust layout to make room for rotated labels
plt.tight_layout()

# Display the plot
plt.show()
