# read questionnaire responses into dataframes and analyse

import pandas as pd 

# %% 

def tsv_to_df(tsv: str) -> pd.DataFrame:

    # extra cols cause parse error; only read in first 2 cols 
    df = pd.read_csv(tsv, sep="\t", usecols=[0,1]) # pyright: ignore

    # remove extra newlines in free text responses
    df.iloc[2,0] = df.iloc[2,0].replace("\n", " ")
    df.iloc[3,0] = df.iloc[3,0].replace("\n", " ")

    return df

# %% 


