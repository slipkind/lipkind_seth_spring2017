import pandas as pd
import numpy as np

# Import Collision Data
collision_data = pd.read_csv('./Data/vehicle_collisions.csv')

# Get name of each Borough
collision_data['BOROUGH'].unique()


# Find number of collisions by subtracting vehicle counts from the right row from the left row (ex: subtract 2 vehicle count from 1 vehicle)
collision_data1 = collision_data.groupby('BOROUGH').apply(lambda x: x['VEHICLE 1 TYPE'].count() - x['VEHICLE 2 TYPE'].count())
collision_data2 = collision_data.groupby('BOROUGH').apply(lambda x: x['VEHICLE 2 TYPE'].count() - x['VEHICLE 3 TYPE'].count())
collision_data3 = collision_data.groupby('BOROUGH').apply(lambda x: x['VEHICLE 3 TYPE'].count() - x['VEHICLE 4 TYPE'].count())
collision_data_more = collision_data.groupby('BOROUGH').apply(lambda x: x['VEHICLE 4 TYPE'].count() + x['VEHICLE 5 TYPE'].count())

# Make a new dataframe from the series
df2 = pd.DataFrame({'One Vehicle': collision_data1, 'Two Vehicle': collision_data2, 'Three Vehicle': collision_data3, 'More Vehicles': collision_data_more})

# write to csv and display the table
df2.to_csv('Question1Part2_AccidentCountsPerBorough.csv')
print(df2.head())
