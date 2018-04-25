import csv
import sys
import numpy

def objectCreate():
	#opens output file
	file = open("../output/pyObject.txt","a+")
	continueQuery = "y"

	loadFile = input ("Did you load the addr.csv in /files? (y/n) ")
	if loadFile == "y":

		#opens CSV
		with open('../files/addr.csv', 'rt') as csvAddr:
	    		readerAddr = csv.reader(csvAddr, delimiter=',', quotechar='|')
	    		readerAddr = list(readerAddr)

	else:
		print ("WTF are you doing here then? Exiting Program")
		sys.exit()


	#Begins Program

	while (continueQuery == "y"):

	#Object type definition
		objectType = input ("Please enter the object type (network, service) ")

	#Network object creation
		if objectType == "network":
			netType = input ("What type of network object? (host, subnet) ")
			if netType == "host":
				for i in range(len(readerAddr)):
					print("object", objectType, readerAddr[i][1], "\n", "host", readerAddr[i][0], file=open("../output/pyObject.txt", "a"))
			else:
				print ("invalid input")
			continueQuery = input ("Do you have any more objects? (y/n) ")
		elif netType == "subnet":
			for i in range(len(readerAddr)):
				print("object", objectType, readerAddr[i][1], "\n", "subnet", readerAddr[i][0], readerAddr[i][2], file=open("../output/pyObject.txt", "a"))
			continueQuery = input ("Do you have any more object files? (y/n) ")

		else:
			print ("Invalid Input")



	#Creates object-groups if requested
	groupQuery = input("Would you like to create an object-group with these servers? (y/n) ")
	while groupQuery == "y":
		groupName = input("Please enter a name for the object group starting with 'OG_': ")
		print("object-group network", groupName, file=open("../output/pyObject.txt","a"))
		for i in range(len(readerAddr)):
			print("network-object object", readerAddr[i][1], file=open("../output/pyObject.txt","a"))
		groupQuery = input("Do you have any more groups? (y/n) ")

	print ("Thank You! Your ASA script is ready at /output/pyObject.txt. Don't forget to Like and Subscribe!")

#def cryptoACL():
#
#def filterACL():
#
#def groupPolicy():
#
#def tunnelGroup():
#
#def cryptoMap():