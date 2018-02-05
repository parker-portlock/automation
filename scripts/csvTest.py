import csv
line_number = 0
column = 0
with open('../files/addr.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    reader = list(reader)
#prints hostname column
for i in range(len(reader)):
    print reader[i][1]

#prints ip column
for i in range(len(reader)):
	print reader[i][0]