import csv
file = open("../output/pyObject.txt","a+")
continueQuery = "y"
line_number = 0

#opens CSV
with open('../files/addr.csv', 'rb') as csvAddr:
    				readerAddr = csv.reader(csvAddr, delimiter=',', quotechar='|')
    				readerAddr = list(readerAddr)

#Begins Program

while (continueQuery == "y"):

#Object type definition
	objectType = raw_input ("Please enter the object type (network, service) ")
	
#Network object creation
	if objectType == "network":
		netType = raw_input ("What type of network object? (host, subnet) ")
		if netType == "host":
			loadFile = raw_input ("Did you load the addr.csv in /files? (y/n) ")
			if loadFile == "y":
				for i in range(len(readerAddr)):
					print >> file, "object", objectType, readerAddr[i][1], "\n", "host", readerAddr[i][0]
			else:
				print "invalid input"
			continueQuery = raw_input ("Do you have any more objects? (y/n) ")
		elif netType == "subnet":
			loadFile = raw_input ("Did you load the object.csv? (y/n) ")
			if loadFile == "y":
				for i in range(len(readerAddr)):
					print >> file, "object", objectType, readerAddr[i][1], "\n", "subnet", readerAddr[i][0], readerAddr[i][2]
			else:
				print "invalid input"

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
print "Thank You! Your ASA script is ready at /output/pyObject.txt. Don't forget to Like and Subscribe!"