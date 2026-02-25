import sys
import os
import unittest
from unittest.mock import patch, ANY

# Add the directory to sys.path to import compile_latex
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'latex_paper_project')))
import compile_latex

class TestCompileLatexArgs(unittest.TestCase):
    @patch('subprocess.run')
    def test_latexmk_args(self, mock_run):
        # Setup mock to succeed
        mock_run.return_value.returncode = 0

        # Run function
        compile_latex.compile_pdf()

        # Check arguments
        mock_run.assert_called_once()
        args, kwargs = mock_run.call_args
        command_list = args[0]

        # Print command list for debugging/verification
        print(f"Command list: {command_list}")

        # Assertions
        self.assertIn("latexmk", command_list)
        self.assertIn("-pdf", command_list)
        self.assertNotIn("-biber", command_list, "Should not contain -biber after fix")

if __name__ == '__main__':
    unittest.main()
