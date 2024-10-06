# convert csv to tsv so latex table import will work properly 

# pandas surrounds text fields with quotation marks if they contain commas 
# these cause csvsimple to fail; convert to tsv to remove them 

import pandas as pd 

# %% 

CSV_QUEST_PATH = "../questionnaires/csv/all_candidates_sorted.csv"
CSV_PARTIES_PATH = "../questionnaires/csv/all_candidates_sorted_memberships.csv"

# %% 

df_quest = pd.read_csv(CSV_QUEST_PATH, header=0)
df_quest.drop(columns="Unnamed: 0", inplace=True)

# %% 

df_parties = pd.read_csv(CSV_PARTIES_PATH, header=0)
df_combined = pd.merge(df_quest, df_parties, on="name")

df_combined.drop(columns="ward_y", inplace=True)
df_combined.rename(columns={"ward_x":"ward"}, inplace=True)
df_combined = df_combined[["name", "ward", "member", "endorsed", "vision", "expertise"]]

# %% 

df_combined.to_csv("../questionnaires/tsv/all_candidates_with_parties.tsv", sep="\t")

