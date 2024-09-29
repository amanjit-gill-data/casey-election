# split all-candidates table by ward 
# yield one csv per ward 

import pandas as pd

# %% 

ALL_WARDS_CSV = "../questionnaires/all_candidates_sorted.csv"
WARD_CSV_PATH = "../questionnaires/wards/"

# %% 

df = pd.read_csv(ALL_WARDS_CSV, header=0)
df.drop(columns="Unnamed: 0", inplace=True)

# %% 

for ward in df['ward'].unique():
    ward_df = df[df['ward'] == ward]
    ward_df.to_csv(WARD_CSV_PATH + ward + ".csv")
    

