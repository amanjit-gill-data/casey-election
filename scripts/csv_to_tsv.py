# convert csv to tsv so latex table import will work properly 

# pandas surrounds text fields with quotation marks if they contain commas 
# these cause csvsimple to fail; convert to tsv to remove them 

import pandas as pd 

# %% 

CSV_PATH = "../questionnaires/csv/all_candidates_sorted.csv"

# %% 

df = pd.read_csv(CSV_PATH, header=0)
df.drop(columns="Unnamed: 0", inplace=True)

# %% 

df.to_csv("../questionnaires/tsv/all_candidates_sorted.tsv", sep="\t")

