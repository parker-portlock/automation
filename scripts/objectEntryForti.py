import csv
file = open("pyFortiObject.txt","a+")
continueQuery = "y"
line_number = 0

#opens CSV
with open('../files/addr.csv', 'rb') as csvAddr:
    				readerAddr = csv.reader(csvAddr, delimiter=',', quotechar='|')
    				readerAddr = list(readerAddr)

#Begins Program

while (continueQuery == "y"):

#Object creation
	loadFile = raw_input ("Did you load the addr.csv in /files? (y/n) ")
	if loadFile == "y":
		for i in range(len(readerAddr)):
			print >> file, "edit", readerAddr[i][1], "\n", "set subnet", readerAddr[i][0] , readerAddr[i][2], "\n", "next"
	else:
		print "invalid input"
	continueQuery = raw_input ("Do you have any more objects? (y/n) ")
			


print "Thank You! Your FortiOS script is ready under the filename pyFortiObject.txt. Don't forget to Like and Subscribe!"