#!/bin/bash

echo "=== Compilation avec latexmk ==="
latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode -file-line-error" main.tex

if [ $? -ne 0 ]; then
    echo "Erreur lors de la compilation avec latexmk"
    exit 1
fi

echo "=== Compilation terminée avec succès ==="
echo "Le fichier PDF a été généré : main.pdf"
