#!/bin/bash

echo "=== Nettoyage des fichiers temporaires ==="
rm -f *.aux *.bbl *.bcf *.blg *.log *.out *.run.xml *.toc *.pdf

echo "=== Première compilation pdflatex ==="
pdflatex -interaction=nonstopmode main.tex
if [ $? -ne 0 ]; then
    echo "Erreur lors de la première compilation pdflatex"
    exit 1
fi

echo "=== Compilation biber ==="
biber main
if [ $? -ne 0 ]; then
    echo "Erreur lors de la compilation biber"
    exit 1
fi

echo "=== Deuxième compilation pdflatex ==="
pdflatex -interaction=nonstopmode main.tex
if [ $? -ne 0 ]; then
    echo "Erreur lors de la deuxième compilation pdflatex"
    exit 1
fi

echo "=== Troisième compilation pdflatex (pour les références) ==="
pdflatex -interaction=nonstopmode main.tex
if [ $? -ne 0 ]; then
    echo "Erreur lors de la troisième compilation pdflatex"
    exit 1
fi

echo "=== Compilation terminée avec succès ==="
echo "Le fichier PDF a été généré : main.pdf"
