import csv
file = open("pyASA.txt","a+")
continueQuery = "y"
line_number = 0

#opens CSV
with open('../files/addr.csv', 'rb') as csvfile:
    				reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    				reader = list(reader)

#Begins Program

while (continueQuery == "y"):

#Object name and type creation
#	objectName = raw_input ("Please enter object name: ")
	objectType = raw_input ("Please enter the object type (network, service) ")
	
#Network object creation
	if objectType == "network":
		netType = raw_input ("What type of network object? (host, subnet) ")
		if netType == "host":
			loadFile = raw_input ("Did you load the addr.csv in /files? (y/n) ")
			if loadFile == "y":
				for i in range(len(reader)):
					print >> file, "object", objectType, reader[i][1], "\n", "host", reader[i][0]
			else:
				print "invalid input"
			continueQuery = raw_input ("Do you have any more objects? (y/n) ")
		elif netType == "subnet":
			loadFile = raw_input ("Did you load the object.csv? (y/n) ")
			if loadFile == "y":
				for i in range(len(reader)):
					print >> file, "object", objectType, reader[i][1], "\n", "subnet", reader[i][0], reader[i][2]
			else:
				print "invalid input"

			continueQuery = raw_input ("Do you have any more object files? (y/n) ")


#		else:
#			print "Invalid Input"
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
print "Thank You! Your ASA script is ready under the filename pyASA.txt. Don't forget to Like and Subscribe!"#