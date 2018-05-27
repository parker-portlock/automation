import sys
import numpy
import csv

#object group function
def CiscoGroup():
#create group for ipsec tunnel
		tunnelQuery = input("Is this a part of a tunnel? (y/n) ")
		if tunnelQuery == "y":
			localGroupName = input("Please enter the name for the local network group: ")
			remoteGroupName = input("Please enter the name for the remote network group: ")
			return localGroupName
			return remoteGroupName
		elif tunnelQuery == "n":
			groupName = input("Please enter a name for the object group: ")
		else:
			print ("Invalid input; exiting...")
			sys.exit()