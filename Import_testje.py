# =============================================================================
# import os
# import sys
# import csv

# absolutepath = os.path.abspath(__file__)
# fileDirectory = os.path.dirname(absolutepath)
# parentDirectory = os.path.dirname(fileDirectory)
# sys.path.append(parentDirectory)
# variable = []

# with open('oefentekst.txt') as csv_file:
#     csv_reader =csv.reader(csv_file, delimiter='t')
    
#     for data in csv_reader: 
#         variable.append(data)
    
# print(variable)
###############################################################################


# Open a file: text
import pandas as pd

df = pd.read_csv (r'C:\Users\NA\OneDrive\PyCharmProjects\Firstproject\username.csv')
print (df)