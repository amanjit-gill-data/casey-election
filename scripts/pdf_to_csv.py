# supply path of pdf 
# csv will be created in same directory as pdf 

import os
import sys
import tabula.io

pdf = sys.argv[1]
basename, _ = os.path.splitext(pdf)
csv = basename + ".csv"

tabula.io.convert_into(pdf, csv, output_format="csv", pages="all")

