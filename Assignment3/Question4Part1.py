import pandas as pd
import numpy as np

# movies database
movies = pd.read_csv('./Data/movies_awards.csv')

# drop any NAN in the awards row
awards = pd.DataFrame(movies['Awards'].dropna())

# Split on all spaces
split_awards = awards['Awards'].apply(lambda x: x.split())
