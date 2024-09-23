# %% 

import pandas as pd 

# %% 

# all data is in first 2 fields (cols)
# some rows have extra fields that contain no info; these cause parse error
# so only read in first two cols 
quest = pd.read_csv("19708.csv", usecols=[0,1])

quest 


