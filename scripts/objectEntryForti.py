import csv
import sys
file = open("pyFortiObject.txt","a+")
continueQuery = "y"
line_number = 0

#opens CSV
with open('../files/addr.csv', 'rt') as csvAddr:
    				readerAddr = csv.reader(csvAddr, delimiter=',', quotechar='|')
    				readerAddr = list(readerAddr)

#Begins Program

while (continueQuery == "y"):

#Object creation
	loadFile = input ("Did you load the addr.csv in /files? (y/n) ")
	if loadFile == "y":
		for i in range(len(readerAddr)):
			print ("edit", readerAddr[i][1], "\n", "set subnet", readerAddr[i][0] , readerAddr[i][2], "\n", "next", file=open("../output/pyFortiObject.txt", "a"))
	else:
		print ("invalid input")
	continueQuery = input ("Do you have any more objects? (y/n) ")
			


print ("Thank You! Your FortiOS script is ready under the filename pyFortiObject.txt. Don't forget to Like and Subscribe!")

sys.exit()