import sys
import numpy
import csv

#object group function
def CiscoGroup():
#create group for ipsec tunnel
	tunnelQuery = input("Is this a part of a tunnel? (y/n) ")
	if tunnelQuery == "y":

		#opens CSVs
		with open('../files/localObjects.csv', 'rt') as csvLoc:
		   		localAddr = csv.reader(csvLoc, delimiter=',', quotechar='|')
		   		localAddr = list(localAddr)

		with open('../files/remoteObjects.csv', 'rt') as csvRem:
			remoteAddr = csv.reader(csvRem, delimiter=',', quotechar='|')
			remoteAddr = list(remoteAddr)

		#creates object group names
		localGroupName = input("Please enter the name for the local network group: ")
		remoteGroupName = input("Please enter the name for the remote network group: ")


		#writes local object-group output
		print("Creating local group...")
		print("object-group network", localGroupName, file=open("../output/ipsec.txt","a"))
		for i in range(len(localAddr)):
			print("network-object object", localAddr[i][1], file=open("../output/ipsec.txt","a"))
		print("exit", file=open("../output/ipsec.txt","a"))
		
		#writes remote object-group output
		print("Creating remote group...")
		print("object-group network", remoteGroupName, file=open("../output/ipsec.txt","a"))
		for i in range(len(remoteAddr)):
			print("network-object object", remoteAddr[i][1], file=open("../output/ipsec.txt","a"))

		print("exit", file=open("../output/ipsec.txt","a"))

	#creates regular object-group
	elif tunnelQuery == "n":
		with open('../files/addr.csv', 'rt') as csvAddr:
			readerAddr = csv.reader(csvAddr, delimiter=',', quotechar='|')
			readerAddr = list(readerAddr)

		groupName = input("Please enter a name for the object group: ")
		print("object-group network", groupName, file=open("../output/ipsec.txt","a"))
		for i in range(len(readerAddr)):
			print("network-object object", readerAddr[i][1], file=open("../output/ipsec.txt","a"))
		
		
	else:
		print ("Invalid input; exiting...")
		sys.exit()