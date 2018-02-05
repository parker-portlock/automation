#extendedACL.py because we know da wae

import csv
file = open("pyACL.txt","a+")
continueQuery = "y"
line_number = 0

#opens CSV
with open('../files/extACL.csv', 'rb') as csvfile:
    				readerACL = csv.reader(csvfile, delimiter=',', quotechar='|')
    				readerACL = list(readerACL)

while (continueQuery == "y"):

	loadFile = raw_input ("Did you load the addr.csv in /files? (y/n) ")
	if loadFile == "y":
		for i in range(len(readerACL)):

		#source rule
			if readerACL[i][8] == "src":
				print >> file, "access-list", readerACL[i][0], "line", readerACL[i][1], readerACL[i][2],readerACL[i][3], "eq", readerACL[i][4],readerACL[i][5],readerACL[i][6]

		#dest rule
			elif readerACL[i][8] == "dest":
				print >> file, "access-list", readerACL[i][0], "line", readerACL[i][1], readerACL[i][2],readerACL[i][3],readerACL[i][4],readerACL[i][6],"eq", readerACL[i][7]
		
		#ip rule
			elif readerACL[i][8] == "ip":
				print >> file, "access-list", readerACL[i][0], "line", readerACL[i][1], readerACL[i][2],readerACL[i][3],readerACL[i][4],readerACL[i][6]
		
		#source group b/c cisco likes to be picky
			elif readerACL[i][8] == "srcgrp":
				print >> file, "access-list", readerACL[i][0], "line", readerACL[i][1], readerACL[i][2],readerACL[i][3],"object-group", readerACL[i][5], readerACL[i][4],readerACL[i][6]


			else:

				print "no direction specified for line", i+1
	else:
		print "invalid input"

	continueQuery = raw_input ("Do you have any more object files? (y/n) ")

print "Thank You! Your ASA script is ready under the filename pyACL.txt. Don't forget to Like and Subscribe!"#