#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv downloadYoutubeEnv
if [ -d "downloadYoutubeEnv" ]; then
    echo "Virtual environment created successfully."
else
    echo "Failed to create virtual environment."
    exit 1
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source downloadYoutubeEnv/bin/activate

# Install required packages
echo "Installing required packages..."
if pip install -r requirements.txt; then
    echo "All packages installed successfully."
else
    echo "Failed to install some packages. Check requirements.txt or pip output for errors."
    deactivate
    exit 1
fi

# Deactivate virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "Setup completed successfully."
