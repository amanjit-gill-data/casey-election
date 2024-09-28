# use the all-candidates csv for analysis 

import pandas as pd

# %% 

df = pd.read_csv("../questionnaires/all_candidates.csv", header=0, index_col=0)

# %% 

df_sorted = df.sort_values(by=["ward", "name"])

# %% 

df_sorted.to_csv("all_candidates_sorted.csv")


