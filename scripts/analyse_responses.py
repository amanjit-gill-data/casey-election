# read each candidate tsv into df and clean 
# extract data from each df; combine into one df for all candidates

import os
import pandas as pd 

# %% 

TSV_DIR = "."

# %% 

def one_tsv_to_df(tsv: str) -> pd.DataFrame:

    """
    read one tsv into df and clean it
    return df
    """

    # extra cols cause parse error; only read in first 2 cols 
    df = pd.read_csv(tsv, sep="\t", usecols=[0,1]) # pyright: ignore

    # remove "Ward" from name of ward 
    df.iloc[0,1] = df.iloc[0,1].replace(" Ward", "")

    # remove extra newlines in free text responses
    df.iloc[2,0] = df.iloc[2,0].replace("\n", " ")
    df.iloc[3,0] = df.iloc[3,0].replace("\n", " ")

    # remove question text from free text responses 

    vision_prompt = "What is your vision for the municipality of the " + \
            "above Council? (maximum 50 words) " 

    expertise_prompt = "What expertise or attributes do you have which " + \
            "would help you in undertaking the role of Councillor? " + \
            "Provide details (maximum 50 words) "

    df.iloc[2,0] = df.iloc[2,0].replace(vision_prompt, "")
    df.iloc[3,0] = df.iloc[3,0].replace(expertise_prompt, "")

    return df

# %% 

def df_to_list(df: pd.DataFrame) -> list[str]:

    """
    extract one candidate's data from df 
    return list
    """

    name = df.iloc[1,1]
    ward = df.iloc[0,1]
    endorsed = df.iloc[6,1]
    vision = df.iloc[2,0]
    expertise = df.iloc[3,0]

    return [name, ward, endorsed, vision, expertise]

# %% 

def all_tsv_to_df(dir: str) -> pd.DataFrame:

    """
    take all candidate tsv files in given dir, extract data and create df 
    return df
    """

    df_list = []

    for file in os.listdir(dir):
        if file.endswith(".tsv"):
            df = one_tsv_to_df(file)
            one_response = df_to_list(df)
            df_list.append(one_response)

    return pd.DataFrame(df_list, 
                        columns=["name", "ward", "endorsed", "vision", "expertise"]) # pyright: ignore

# %% 

def main():

    df = all_tsv_to_df(TSV_DIR)
    df.to_csv("candidates.csv")

# %% 

if __name__ == "__main__":
    main()

