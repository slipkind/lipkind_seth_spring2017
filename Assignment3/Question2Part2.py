import pandas as pd
import numpy as np

# Import employee compensation data
employee_compensation = pd.read_csv('./Data/employee_compensation.csv')

# remove any fiscal year, only include calendar
cal_comp = employee_compensation[(employee_compensation['Year Type'] == 'Calendar')]

# Group by Job Family and Employee Identifier
cal_group = cal_comp.groupby(['Job Family', 'Employee Identifier'])

# Find the means of the salaries, overtime, total comp and total benefits
mean_cal = cal_group[[ 'Salaries', 'Overtime',  'Total Compensation', 'Total Benefits']].mean()

# Only include rows whose overtime was greater than 5% of their salary
overtime_cal = mean_cal[mean_cal['Overtime']/mean_cal['Salaries'] > .05]

# Create a percentage benefits column
overtime_cal['Percentage Benefits'] = (overtime_cal['Total Benefits']/overtime_cal['Total Compensation'])

# Sort in descending order
result = overtime_cal.sort(['Percentage Benefits'], ascending=False)

# Write to csv and print top rows
result.to_csv('Question2Part2_Benefits.csv')
print(result.head())
