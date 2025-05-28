# Research Paper LaTeX Project

This repository contains the LaTeX source files and compilation script for the research paper: "Effet comparatif de l’extrait butanolique de la plante Stachys mialhesi avec les vitamines B9 et B12 sur quelques paramètres biochimiques et la structure de l’aorte chez des souris induites par une hyperhomocystéinémie".

The project is structured within the `latex_paper_project/` directory.

## Compilation

To compile the LaTeX document into a PDF:
1. Navigate to the `latex_paper_project/` directory.
2. Ensure you have Python 3, TeX Live (with `pdflatex` and `biber`), and all necessary LaTeX packages installed.
3. Run the compilation script: `python compile_latex.py`
4. The output PDF will be `main.pdf` in the `latex_paper_project/` directory.

## Automated Workflow (GitHub Actions)

This project uses GitHub Actions to automatically compile the LaTeX document (`latex_paper_project/main.tex`) into a PDF.

- **Trigger**: The workflow runs automatically on every `push` to any branch and on every `pull_request` targeting the main branches.
- **Process**:
  1. Sets up a TeX Live environment.
  2. Installs necessary LaTeX packages.
  3. Checks out the repository code.
  4. Runs the `python latex_paper_project/compile_latex.py` script.
- **Success**: If the compilation is successful, the generated PDF (`main.pdf`) will be available as an artifact that can be downloaded from the workflow run's summary page.
- **Failure**: If the compilation fails:
  - A GitHub issue will be automatically created, titled "LaTeX Compilation Failed".
  - The issue will be assigned to the user who triggered the workflow.
  - A detailed compilation log (`compilation_log.txt`) will be uploaded as an artifact to the workflow run, which can be used to diagnose the error.

You can view the status of the workflows under the "Actions" tab of this repository.