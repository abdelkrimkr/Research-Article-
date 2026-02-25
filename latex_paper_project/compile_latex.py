import subprocess
import os
import sys

# Define ANSI colors for UX improvement
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cprint(message, color=None):
    """Prints a message in color if supported or forced."""
    use_color = sys.stdout.isatty() or os.environ.get('FORCE_COLOR')
    if use_color and color:
        print(f"{color}{message}{Colors.ENDC}")
    else:
        print(message)

main_tex_file = "main"

def compile_pdf():
    try:
        cprint(f"🚀 Running latexmk on {main_tex_file}.tex...", Colors.OKCYAN)
        # Command to compile LaTeX document using latexmk, ensuring PDF generation,
        # using pdflatex with specific flags, and calling biber.
        latexmk_command = [
            "latexmk",
            "-pdf",
            "-pdflatex=pdflatex -interaction=nonstopmode -file-line-error",
            f"{main_tex_file}.tex"
        ]
        subprocess.run(latexmk_command, check=True, capture_output=True, text=True)

        cprint(f"✅ PDF compiled successfully: {main_tex_file}.pdf", Colors.OKGREEN)

    except subprocess.CalledProcessError as e:
        cprint(f"❌ An error occurred during latexmk compilation: {e}", Colors.FAIL)
        cprint(f"Command '{' '.join(e.cmd)}' returned non-zero exit status {e.returncode}.", Colors.FAIL)
        # stdout and stderr are already captured as text due to text=True
        if e.stdout:
            cprint(f"Stdout:\n{e.stdout}", Colors.FAIL)
        if e.stderr:
            cprint(f"Stderr:\n{e.stderr}", Colors.FAIL)
        # Suggest checking the latexmk log file for detailed errors
        cprint(f"⚠️  Please check the log file '{main_tex_file}.log' for more details.", Colors.WARNING)
        sys.exit(1) # Exit with error code
    except FileNotFoundError as e:
        cprint(f"❌ Error: Required command not found: {e.filename}", Colors.FAIL)
        cprint(f"👉 Please ensure latexmk, pdflatex, and biber are installed and in your PATH.", Colors.FAIL)
        sys.exit(1) # Exit with error code
    except Exception as e:
        cprint(f"❌ An unexpected error occurred: {e}", Colors.FAIL)


if __name__ == "__main__":
    # Ensure the script is run from the directory where main.tex is located,
    # or adjust paths accordingly. For this project, it's the root.
    # os.chdir(os.path.dirname(os.path.abspath(__file__))) # Optional: if script can be run from elsewhere
    compile_pdf()
