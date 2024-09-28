# pdf_to_csv.py 
# convert pdf(s) to csv

import os
import tabula.io
import pandas as pd

# %% 


def convert_one_pdf(pdf: str) -> None:

    """
    convert one pdf to tsv
    output tsv lands in same dir as pdf 
    """

    basename, _ = os.path.splitext(pdf)
    tsv = basename + ".tsv"

    tabula.io.convert_into(pdf, tsv, output_format="tsv", pages="all")

# %% 

def clean_tsv(tsv: str) -> None:

    """
    remove carriage returns from free text responses
    otherwise words are missing when printed to stdout
    """

    # text responses have words missing when printed, unless CRs are removed 
    with open(tsv, "r+") as file:
        orig_text = file.read()
        new_text = orig_text.replace("\r", " ")
        file.seek(0)
        file.truncate()
        file.write(new_text)

# %% 

def tsv_to_df(tsv: str) -> pd.DataFrame:

    # some rows have extra columns that cause parse error
    # only read in first 2 columns 
    df = pd.read_csv(tsv, sep="\t", usecols=[0,1]) # pyright: ignore

    # extra newlines within text responses remain even after CRs were removed 
    # need to replace in specific cells
    df.iloc[2,0] = df.iloc[2,0].replace("\n", " ")
    df.iloc[3,0] = df.iloc[3,0].replace("\n", " ")

    return df

# %% 

def convert_pdfs(in_dir: str, out_dir: str):

    """
    convert all pdfs in dir to csv 
    output csvs land in new dir 

    arguments:
        in_dir: dir containing pdfs 
        out_dir: target dir for csvs; created if needed 

    returns:
        None 
    """

    pass 

# %% 

def main():
    convert_one_pdf("/home/ag/projects/casey-election/scripts/19708.pdf")
    clean_tsv("./19708.tsv")
    df = tsv_to_df("./19708.tsv")

    print(df.iloc[2,0])
    print(df.iloc[3,0])

# %% 

if __name__ == "__main__":
    main()

# %% 

main()



