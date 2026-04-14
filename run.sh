#!/bin/bash

# Create venv if missing
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the API
uvicorn main:app --host 0.0.0.0 --port 8000
