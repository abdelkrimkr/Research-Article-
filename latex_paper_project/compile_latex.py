import subprocess
import os
import sys # Import sys module

main_tex_file = "main" # No .tex extension here

def compile_pdf():
    try:
        print(f"Running latexmk on {main_tex_file}.tex...")
        # Command to compile LaTeX document using latexmk, ensuring PDF generation,
        # using pdflatex with specific flags, and calling biber.
        latexmk_command = [
            "latexmk",
            "-pdf",
            "-pdflatex=pdflatex -interaction=nonstopmode -file-line-error",
            "-biber",
            f"{main_tex_file}.tex"
        ]
        subprocess.run(latexmk_command, check=True, capture_output=True, text=True)

        print(f"PDF compiled successfully with latexmk: {main_tex_file}.pdf")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during latexmk compilation: {e}")
        print(f"Command '{' '.join(e.cmd)}' returned non-zero exit status {e.returncode}.")
        # stdout and stderr are already captured as text due to text=True
        if e.stdout:
            print(f"Stdout:\n{e.stdout}")
        if e.stderr:
            print(f"Stderr:\n{e.stderr}")
        # Suggest checking the latexmk log file for detailed errors
        print(f"Please check the log file '{main_tex_file}.log' for more details.")
        sys.exit(1) # Exit with error code
    except FileNotFoundError as e:
        print(f"Error: A required command was not found: {e.filename}. Please ensure latexmk, pdflatex, and biber are installed and in your PATH.")
        sys.exit(1) # Exit with error code
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Ensure the script is run from the directory where main.tex is located,
    # or adjust paths accordingly. For this project, it's the root.
    # os.chdir(os.path.dirname(os.path.abspath(__file__))) # Optional: if script can be run from elsewhere
    compile_pdf()
