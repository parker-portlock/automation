import csv
import sys
import numpy
file = open("../output/pyObject.txt","a+")
continueQuery = "y"

#python-numpy package required

loadFile = raw_input ("Did you load the addr.csv in /files? (y/n) ")
if loadFile == "y":

	#opens CSV
	with open('../files/addr.csv', 'rb') as csvAddr:
    		readerAddr = csv.reader(csvAddr, delimiter=',', quotechar='|')
    		readerAddr = list(readerAddr)

else:
	print "WTF are you doing here then? Exiting Program"
	sys.exit()


#Begins Program

while (continueQuery == "y"):

#Object type definition
	objectType = raw_input ("Please enter the object type (network, service) ")

#Network object creation
	if objectType == "network":
		netType = raw_input ("What type of network object? (host, subnet) ")
		if netType == "host":
			for i in range(len(readerAddr)):
				print >> file, "object", objectType, readerAddr[i][1], "\n", "host", readerAddr[i][0]
		else:
			print "invalid input"
		continueQuery = raw_input ("Do you have any more objects? (y/n) ")
	elif netType == "subnet":
		for i in range(len(readerAddr)):
			print >> file, "object", objectType, readerAddr[i][1], "\n", "subnet", readerAddr[i][0], readerAddr[i][2]
		continueQuery = raw_input ("Do you have any more object files? (y/n) ")

	else:
		print "Invalid Input"


		

	
#	
#	
#	#service object creation
#	elif objectType == "service":
#		servProto = raw_input ("What is the protocol? (tcp, udp)")
#		if servProto == "tcp":
#			portType = raw_input ("Source or Destination port? ")
#			if portType == "source":
#				portNumber = raw_input ("Please enter the source port number: ")
#				print "OUTPUT HERE"
#			elif portType == "destination":
#				portNumber = raw_input ("Please enter the destination port number: ")
#				print "OUTPUT HERE"
#			else:
#				print "Invalid Input"
#		elif servProto == "udp":
#			portType = raw_input ("Source or Destination port? ")
#			if portType == "source":
#				portNumber = raw_input ("Please enter the source port number: ")
#				print "OUTPUT HERE"
#			elif portType == "destination":
#				portNumber = raw_input ("Please enter the destination port number: ")
#				print "OUTPUT HERE"
#			else:
#				print "Invalid Input"
#		else:
#			print "Invalid Input"
#	else:
#		print "Invalid Input"



groupQuery = raw_input("Would you like to create an object-group with these servers? (y/n) ")
while groupQuery == "y":
	groupName = raw_input("Please enter a name for the object group starting with 'OG_': ")
	print >> file, "object-group network", groupName
	for i in range(len(readerAddr)):
		print >> file, "network-object object", readerAddr[i][1]
	groupQuery = raw_input("Do you have any more groups? (y/n) ")

print "Thank You! Your ASA script is ready at /output/pyObject.txt. Don't forget to Like and Subscribe!"