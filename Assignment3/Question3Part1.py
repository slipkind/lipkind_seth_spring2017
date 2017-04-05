import pandas as pd
import numpy as np

# Import cricket data
cricket = pd.read_csv('./Data/cricket_matches.csv')

# Only include if home team was the winner
cricket_home_winners = cricket[(cricket['home'] == cricket['winner'])]

# Pull out the rows where the winners were the home team based on inning
cricket_home_inning_1 = cricket_home_winners[(cricket['home'] == cricket['innings1'])]
cricket_home_inning_2 = cricket_home_winners[(cricket['home'] == cricket['innings2'])]

# create home innings data frames for innings 1 and 2, then combine
cricket_home_inning_1_runs = cricket_home_inning_1[['home', 'innings1_runs']]
cricket_home_inning_2_runs = cricket_home_inning_2[['home', 'innings2_runs']]
cricket_home_both_innings = cricket_home_inning_1_runs.append(cricket_home_inning_2_runs)

# group by home and find the mean
average_cricket = cricket_home_both_innings.groupby('home').mean()

# calculate the average of each row and print to csv
average_cricket.mean(axis=1).to_csv('Question3Part1_cricket.csv')

# print a few rows to the screen
print(average_cricket.head())
