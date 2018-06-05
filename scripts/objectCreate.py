import csv
import sys


def CiscoTunObject():
	#opens output file
	#file = open("../output/ipsec.txt","a+")
	#continueQuery = "y"



	#while (continueQuery == "y"):

#Object type definition
		tunnelObject = input ("Are these objects for an IPsec Tunnel? (y/n) ")
		if tunnelObject == "y":

#CSV READ
			loadFile = input ("Did you load the localObjects.csv and remoteObjects.csv in /files? (y/n) ")
			if loadFile == "y":

#opens Local and remote CSV
				with open('../files/localObjects.csv', 'rt') as csvLoc:
			    		localAddr = csv.reader(csvLoc, delimiter=',', quotechar='|')
			    		localAddr = list(localAddr)

				with open('../files/remoteObjects.csv', 'rt') as csvRem:
			    		remoteAddr = csv.reader(csvRem, delimiter=',', quotechar='|')
			    		remoteAddr = list(remoteAddr)
			else:
				print ("WTF are you doing here then? Exiting Program")
				sys.exit()
#Local object Creation
			print("Let's create the local objects.")
			objectType = input ("Please enter the object type (network, service) ")
			if objectType == "network":
				netType = input ("What type of network object? (host, subnet) ")
				if netType == "host":
					for i in range(len(localAddr)):
						print("object", objectType, localAddr[i][1], "\n", "host", localAddr[i][0], file=open("../output/ipsec.txt", "a"))
				
				elif netType == "subnet":
					for i in range(len(localAddr)):
						print("object", objectType, localAddr[i][1], "\n", "subnet", localAddr[i][0], localAddr[i][2], file=open("../output/ipsec.txt", "a"))
			else:
				print ("Invalid input; exiting...")
				sys.exit()

#Remote object Creation
			print("Let's create the remote objects.")
			objectType = input ("Please enter the object type (network, service) ")
			if objectType == "network":
				netType = input ("What type of network object? (host, subnet) ")
				if netType == "host":
					for i in range(len(remoteAddr)):
						print("object", objectType, remoteAddr[i][1], "\n", "host", remoteAddr[i][0], file=open("../output/ipsec.txt", "a"))
			
				elif netType == "subnet":
					for i in range(len(remoteAddr)):
						print("object", objectType, remoteAddr[i][1], "\n", "subnet", remoteAddr[i][0], remoteAddr[i][2], file=open("../output/ipsec.txt", "a"))
				
			else:
				print ("Invalid input; exiting...")
				sys.exit()

		elif tunnelObject == "n":
			loadFile = input ("Did you load the localObjects.csv and remoteObjects.csv in /files? (y/n) ")
			if loadFile == "y":

#opens CSV
				with open('../files/objects.csv', 'rt') as csvObj:
			    		objAddr = csv.reader(csvObj, delimiter=',', quotechar='|')
			    		objAddr = list(objAddr)

			else:
				print ("WTF are you doing here then? Exiting Program")
				sys.exit()


#creates objects		
			objectType = input ("Please enter the object type (network, service) ")
			if objectType == "network":
				netType = input ("What type of network object? (host, subnet) ")
				if netType == "host":
					for i in range(len(objAddr)):
						print("object", objectType, objAddr[i][1], "\n", "host", objAddr[i][0], file=open("../output/ipsec.txt", "a"))
				else:
					print ("invalid input")
	
			elif netType == "subnet":
				for i in range(len(localAddr)):
					print("object", objectType, objAddr[i][1], "\n", "subnet", objAddr[i][0], objAddr[i][2], file=open("../output/ipsec.txt", "a"))
			else:
				print ("Invalid input; exiting...")
				sys.exit()