file = open("pyASA.txt","a+")
continueQuery = "y"
while (continueQuery == "y"):

#Object name and type creation
	objectName = raw_input ("Please enter object name: ")
	objectType = raw_input ("Please enter the object type (network, service) ")
	
#Network object creation
	if objectType == "network":
		netType = raw_input ("What type of network object? (host, subnet) ")
		if netType == "host":
			netHost = raw_input ("Please enter the IPv4 host address: ")
			print "object", objectType, objectName, "\n", "host", netHost
			print >>file, "object", objectType, objectName, "\n", "host", netHost
			continueQuery = raw_input ("Do you have any more objects? (y/n) ")
		elif netType == "subnet":
			netSubnet = raw_input ("Please enter the subnet in network (space) mask form: ")
			print "object", objectType, objectName, "\n", "subnet", netSubnet
			print >>file, "object", objectType, objectName, "\n", "subnet", netSubnet, "\n"
			continueQuery = raw_input ("Do you have any more objects? (y/n) ")
		else:
			print "Invalid Input"
	
	
	#service object creation
	elif objectType == "service":
		servProto = raw_input ("What is the protocol? (tcp, udp)")
		if servProto == "tcp":
			portType = raw_input ("Source or Destination port? ")
			if portType == "source":
				portNumber = raw_input ("Please enter the source port number: ")
				print "OUTPUT HERE"
			elif portType == "destination":
				portNumber = raw_input ("Please enter the destination port number: ")
				print "OUTPUT HERE"
			else:
				print "Invalid Input"
		elif servProto == "udp":
			portType = raw_input ("Source or Destination port? ")
			if portType == "source":
				portNumber = raw_input ("Please enter the source port number: ")
				print "OUTPUT HERE"
			elif portType == "destination":
				portNumber = raw_input ("Please enter the destination port number: ")
				print "OUTPUT HERE"
			else:
				print "Invalid Input"
		else:
			print "Invalid Input"
	else:
		print "Invalid Input"
print "Thank You! Your ASA script is ready under the filename pyASA.txt. Don't forget to Like and Subscribe!"