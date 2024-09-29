# sort all-candidates csv by ward, then candidate name 

# including this in the pdf-tsv-df-csv process would lose the data that was 
# manually added for six corrupted pdfs 

import pandas as pd

# %% 

df = pd.read_csv("../questionnaires/all_candidates.csv", header=0, index_col=0)

# %% 

df_sorted = df.sort_values(by=["ward", "name"])

# %% 

df_sorted.to_csv("all_candidates_sorted.csv")


