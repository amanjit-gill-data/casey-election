# convert pdf files to tsv

import os
import sys
import tabula.io

# %% 

PDF_DIR = sys.argv[1]

# %% 

def convert_all_pdf(dir: str) -> None:

    """
    convert all the pdfs in given directory to tsv
    """
    tabula.io.convert_into_by_batch(dir, output_format="tsv", pages="all")

# %% 

def clean_one_tsv(tsv: str) -> None:

    """
    remove carriage returns from free text responses
    otherwise words are cut off when printed to stdout
    """

    # opening file twice (once to read, once to write) may cause race condition
    # so open file only once for both read+write 
    with open(tsv, "r+") as file:
        orig_text = file.read()
        new_text = orig_text.replace("\r", " ")
        file.seek(0)
        file.truncate()
        file.write(new_text)

# %% 

def clean_all_tsv(dir: str) -> None:

    """
    clean all tsv files in given directory 
    """

    for file in os.listdir(dir):
        if file.endswith(".tsv"):
            clean_one_tsv(file)

# %% 

def main():

    convert_all_pdf(PDF_DIR)
    clean_all_tsv(PDF_DIR)   

# %% 

if __name__ == "__main__":
    main()

