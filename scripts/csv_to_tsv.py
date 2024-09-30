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

# replace & and ! as these cause latex to not build

df = df.replace("&", "and", regex=True)
df = df.replace("!", ".", regex=True)

# %% 

df.to_csv("../questionnaires/csv/all_candidates_sorted.tsv", sep="\t")

