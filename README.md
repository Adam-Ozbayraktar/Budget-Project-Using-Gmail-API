# Budgeting Software using Gmail API


This software downloads email attachements from your bank containing your bank statements, it then parses the pdf document into a csv and the csv is exported into a database and is displayed using a combination of Flask, HTML and CSS.

## How to Set-up:

1. Install pipenv from pip 
2. If on windows, start pipenv in directory using command: pipenv shell
3. To install all packages required use command: pipenv install 
4. Go [here](https://developers.google.com/gmail/api/quickstart/python) to set up gmail API
5. Copy credentials.json to file directory
6. Run "Budget_Program.py"

*Please note that due to the fact that a custom parser has to exsist 
for each bank and each pdf structure, this program only currently works with Standard Bank in South Africa,
but if the parser is modified the rest of the program will work for any bank.*
