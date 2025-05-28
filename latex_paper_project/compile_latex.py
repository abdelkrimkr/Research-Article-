import subprocess
import os

main_tex_file = "main" # No .tex extension here

def compile_pdf():
    try:
        print(f"Running pdflatex on {main_tex_file}.tex (1st pass)...")
        # Using shell=True can be a security hazard if command components are from external input.
        # Here, main_tex_file is hardcoded, so it's less of a risk.
        # For robustness, especially if main_tex_file could change, avoid shell=True.
        # However, pdflatex and biber are often easier to get working with shell=True
        # due to PATH issues in some environments. Given this is a controlled environment,
        # direct command list is preferred.
        subprocess.run(["pdflatex", "-interaction=nonstopmode", f"{main_tex_file}.tex"], check=True, capture_output=True, text=True)

        print(f"Running biber on {main_tex_file}...")
        subprocess.run(["biber", main_tex_file], check=True, capture_output=True, text=True) # biber usually takes the filename without extension

        print(f"Running pdflatex on {main_tex_file}.tex (2nd pass)...")
        subprocess.run(["pdflatex", "-interaction=nonstopmode", f"{main_tex_file}.tex"], check=True, capture_output=True, text=True)

        print(f"Running pdflatex on {main_tex_file}.tex (3rd pass)...")
        subprocess.run(["pdflatex", "-interaction=nonstopmode", f"{main_tex_file}.tex"], check=True, capture_output=True, text=True)

        print(f"PDF compiled successfully: {main_tex_file}.pdf")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during compilation: {e}")
        print(f"Command '{' '.join(e.cmd)}' returned non-zero exit status {e.returncode}.")
        # stdout and stderr are already captured as text due to text=True
        if e.stdout:
            print(f"Stdout:\n{e.stdout}")
        if e.stderr:
            print(f"Stderr:\n{e.stderr}")
        # Attempt to provide more specific feedback for common LaTeX errors
        if e.stdout: # pdflatex often prints errors to stdout
            if "! LaTeX Error:" in e.stdout:
                print("A LaTeX error was detected. Please check the log file for more details.")
            elif "Undefined citation" in e.stdout:
                 print("Undefined citations detected. Check your .bib file and citation keys.")
    except FileNotFoundError as e:
        print(f"Error: A required command was not found: {e.filename}. Please ensure pdflatex and biber are installed and in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Ensure the script is run from the directory where main.tex is located,
    # or adjust paths accordingly. For this project, it's the root.
    # os.chdir(os.path.dirname(os.path.abspath(__file__))) # Optional: if script can be run from elsewhere
    compile_pdf()
