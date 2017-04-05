import pandas as pd
import numpy as np

# import collision data from the data set
collision_data = pd.read_csv('./Data/vehicle_collisions.csv')

# replace all NAN with empty strings
collision_data['BOROUGH'].replace(np.nan,'',regex=True)

# Convert date column to datetime format
collision_data['DATE']= pd.to_datetime(collision_data['DATE'])

# Add columns for month and year
collision_data['YEAR'] = collision_data['DATE'].dt.year
collision_data['MONTH'] = collision_data['DATE'].dt.month

col_2016 = collision_data[collision_data['YEAR'] == 2016]
data_frame_2016 = pd.DataFrame()

# Get all manhattan data, then group by month
all_man = col_2016[col_2016['BOROUGH'] == 'MANHATTAN']
all_man = all_man.groupby('MONTH')['UNIQUE KEY'].nunique()
data_frame_2016['MANHATTAN'] = all_man

# Get all ny city accidents
all_2016 = col_2016.groupby('MONTH')['UNIQUE KEY'].nunique()
data_frame_2016['NYC'] = all_2016

# Calculate the percentage of NYC accidents from Manhattan, then write to csv
data_frame_2016['Percentage'] = (data_frame_2016['MANHATTAN']/data_frame_2016['NYC'])
data_frame_2016.to_csv('Question1Part1_2016_Manhattan_Percentages.csv')
print(data_frame_2016.head())
