#!/bin/bash
for i in *.tex; do
    [ -f "$i" ] || break
    pdflatex $i
    pdf2svg ${i%.tex}.pdf ${i%.tex}.svg
done
rm *.aux
rm *.log
rm *.pdf
rm *.fls
rm *.fdb_latexmk
