#!/bin/bash

# Check if Python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found"
    exit
fi

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found"
    exit
fi

# Check if rclone is installed
if ! command -v rclone &> /dev/null
then
    echo "rclone could not be found"
    exit
fi

# Set up virtual environment
if [ ! -d "venv" ]
then
    python3 -m venv venv
fi
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Check for rclone configuration file
if [ ! -f "rclone.conf" ]
then
    echo "rclone configuration file not found"
    exit
fi

# Apply Django migrations
python manage.py migrate

# Start Django development server
python manage.py runserver