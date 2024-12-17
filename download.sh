#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Virtual environment path
VENV_DIR="downloadYoutubeEnv"
PYTHON_SCRIPT="downloadYoutube.py"

# Check if the virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Error: Virtual environment '$VENV_DIR' does not exist. Run the setup script first."
    exit 1
fi

# Check if the Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: Python script '$PYTHON_SCRIPT' not found."
    exit 1
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Run the Python script
echo "Starting the download script..."
python "$PYTHON_SCRIPT"

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "Download process completed successfully."
