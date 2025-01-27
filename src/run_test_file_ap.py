import subprocess
import os

# Define the path to the test file
test_file_path = os.path.join(os.path.dirname(__file__), 'test_file_ap.py')

# Run the test file
subprocess.run(['python', test_file_path])