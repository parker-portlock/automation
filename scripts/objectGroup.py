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
		with open('../files/localObjects.csv', 'rt') as csvRem:
		   		remoteAddr = csv.reader(csvRem, delimiter=',', quotechar='|')
		  		remoteAddr = list(remoteAddr)

		#creates object group names
		localGroupName = input("Please enter the name for the local network group: ")
		remoteGroupName = input("Please enter the name for the remote network group: ")

		#sends back to master
		return localGroupName
		return remoteGroupName

		#writes local object-group output
		print("object-group network", groupName, file=open("../output/pyObject.txt","a"))
		for i in range(len(localAddr)):
			print("network-object object", localAddr[i][1], file=open("../output/pyObject.txt","a"))
		
		#writes remote object-group output
		print("object-group network", groupName, file=open("../output/pyObject.txt","a"))
		for i in range(len(remoteAddr)):
			print("network-object object", remoteAddr[i][1], file=open("../output/pyObject.txt","a"))
			
	elif tunnelQuery == "n":
		groupName = input("Please enter a name for the object group: ")
	else:
		print ("Invalid input; exiting...")
		sys.exit()