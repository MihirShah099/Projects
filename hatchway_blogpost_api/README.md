# Hatchways back-end Developer Challenge

## Requirement
- Install python 3.9.1
- (recommended) after copying the folders and files within a directory, create  virtual environment by typing `python3 -m venv env`. Activate the environnement by typing `source env/bin/activate`

## command to install requirement file
install the python packages : `pip3 install -r requirements.txt`

## How to run command
To start the back-end: `uvicorn src.main:app`. the port used is 8000
To run all unitest: `python3 -m unittest discover -p '*_test.py'`