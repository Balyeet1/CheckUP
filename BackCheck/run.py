import os
from waitress import serve
from my_app import app  # Import your app
import logging

# Run from the same directory as this script
this_files_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(this_files_dir)

serve(app, port=8080)

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

