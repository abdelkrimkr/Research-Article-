import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO

# Add the directory to sys.path to import compile_latex
# Assuming tests/ is at the root, and latex_paper_project/ is also at root.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'latex_paper_project')))
import compile_latex

class TestCompileLatexUX(unittest.TestCase):
    @patch('subprocess.run')
    @patch('sys.stdout', new_callable=StringIO)
    def test_success_output(self, mock_stdout, mock_run):
        # Setup mock to succeed
        mock_run.return_value.returncode = 0

        # Run the function with FORCE_COLOR=1
        with patch.dict(os.environ, {'FORCE_COLOR': '1'}):
            compile_latex.compile_pdf()

        # Check output
        output = mock_stdout.getvalue()
        # Check for success emoji and green color code (approximate check)
        self.assertIn("✅", output)
        self.assertIn("PDF compiled successfully", output)
        self.assertIn("\033[92m", output)

    @patch('subprocess.run')
    @patch('sys.stdout', new_callable=StringIO)
    def test_failure_output_file_not_found(self, mock_stdout, mock_run):
        # Setup mock to fail with FileNotFoundError (simulating missing latexmk)
        mock_run.side_effect = FileNotFoundError(2, "No such file or directory", "latexmk")

        # Run function, expecting exit(1)
        with self.assertRaises(SystemExit):
            with patch.dict(os.environ, {'FORCE_COLOR': '1'}):
                compile_latex.compile_pdf()

        output = mock_stdout.getvalue()
        self.assertIn("❌", output)
        # Note: I'll match slightly generic message to be safe
        self.assertIn("Error", output)
        self.assertIn("latexmk", output)
        # Check for red color code
        self.assertIn("\033[91m", output)

    @patch('subprocess.run')
    @patch('sys.stdout', new_callable=StringIO)
    def test_failure_output_called_process_error(self, mock_stdout, mock_run):
        # Setup mock to fail with CalledProcessError
        import subprocess
        mock_run.side_effect = subprocess.CalledProcessError(1, ["latexmk"], output="Some log output", stderr="Some error output")

        # Run function, expecting exit(1)
        with self.assertRaises(SystemExit):
             with patch.dict(os.environ, {'FORCE_COLOR': '1'}):
                compile_latex.compile_pdf()

        output = mock_stdout.getvalue()
        self.assertIn("❌", output)
        self.assertIn("An error occurred during latexmk compilation", output)
        self.assertIn("\033[91m", output)

if __name__ == '__main__':
    unittest.main()
