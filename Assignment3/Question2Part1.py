import pandas as pd
import numpy as np

# Read in the employee compensation data files
employee_compensation = pd.read_csv('./Data/employee_compensation.csv')

# group the employees by organization group and department and find the mean
grouped_employee = employee_compensation.groupby(['Organization Group','Department']).mean()

# Create a data frame with the total compensation and transpose
grouped_employee_compensation = pd.DataFrame([grouped_employee['Total Compensation']]).T

# find the largest compensation and write to csv
highest_comp = grouped_employee_compensation['Total Compensation'].nlargest(len(grouped_employee_compensation))

highest_comp.to_csv('Question2Part1_EmployeeCompensation.csv')
print(highest_comp.head())
