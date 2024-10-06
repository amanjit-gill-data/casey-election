# split all-candidates table by ward 
# yield one tsv per ward 

import pandas as pd

# %% 

ALL_WARDS_TSV = "../questionnaires/tsv/all_candidates_with_parties.tsv"
WARD_TSV_PATH = "../questionnaires/tsv/wards/"

# %% 

df = pd.read_csv(ALL_WARDS_TSV, header=0, sep="\t")
df.drop(columns="Unnamed: 0", inplace=True)

# %% 

for ward in df['ward'].unique():
    ward_df = df[df['ward'] == ward]
    ward_df.to_csv(WARD_TSV_PATH + ward + ".tsv", sep="\t")
    
