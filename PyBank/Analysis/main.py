# Your task is to create a Python script that analyzes 
# the records to calculate each of the following:

# 1. The total number of months included in the dataset
# 2. The net total amount of "Profit/Losses" over the 
# entire period
# 3. Calculate the changes in "Profit/Losses" over the
# entire period
# 4. The greatest increase in profits (date and amount)
# over the entire period
# 5. The greatest decrease in profits (date and amount)
# over the entire period

# Import dependencies
import os
import csv
from typing import ClassVar

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
    if row[0] == 'Jan-{year}'
        
