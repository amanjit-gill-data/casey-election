#!/usr/bin/bash

ward_tsv_path="../questionnaires/tsv/wards"
ward_pdf_path="../deliverables/ward_tables/"

for file in ${ward_tsv_path}/*.tsv; do
  
  ward=`basename "$file" | sed "s/.tsv//g"`
  pdf=`basename "$file" | sed "s/.tsv/.pdf/g"`

  sed -i "s|WARDNAME|${ward}|g" ward_table.tex
  sed -i "s|FILEPATH|${file}|g" ward_table.tex

  tectonic ward_table.tex 
  mv ward_table.pdf "$pdf"  

  sed -i "s|${file}|FILEPATH|g" ward_table.tex
  sed -i "s|${ward}|WARDNAME|g" ward_table.tex

done 

mkdir -p "$ward_pdf_path"
mv *.pdf "$ward_pdf_path"


