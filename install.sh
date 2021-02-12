#!/usr/bin/bash

# Author: Nicolas Nunez 2021-12-02

# Create directories
mkdir -p ~/.local/opt/tasky
mkdir -p ~/.local/bin

# Copy project
cp -r ./tasky_app ~/.local/opt/tasky/tasky_app
cp -r main.py ~/.local/opt/tasky/main.py
cp -r requirements.txt ~/.local/opt/tasky/requirements.txt

# Install dependencies
cd ~/.local/opt/tasky
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
deactivate

# Create symbolic link to app
ln -s ~/.local/opt/tasky/main.py ~/.local/bin/tasky
export PATH="$PATH:~/.local/bin"
