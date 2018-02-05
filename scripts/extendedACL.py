#extendedACL.py because we know da wae

import csv
file = open("pyASA.txt","a+")
continueQuery = "y"
line_number = 0

#opens CSV
with open('../files/extACL.csv', 'rb') as csvfile:
    				reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    				reader = list(reader)