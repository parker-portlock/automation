import csv
import sys


def CiscoTunObject():
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
			objectType = "network"
			print("Let's create the local objects.")
			for i in range(len(localAddr)):
				netType = localAddr[i][2]
				if netType =='':
					print("object", objectType, localAddr[i][1], "\n", "host", localAddr[i][0], file=open("../output/ipsec.txt", "a"))
				elif netType !='':
					print("object", objectType, localAddr[i][1], "\n", "subnet", localAddr[i][0], localAddr[i][2], file=open("../output/ipsec.txt", "a"))

#Remote object Creation
			print("Let's create the remote objects.")
			for i in range(len(remoteAddr)):
				netType = localAddr[i][2]
				if netType =='':
					print("object", objectType, remoteAddr[i][1], "\n", "host", remoteAddr[i][0], file=open("../output/ipsec.txt", "a"))
				elif netType != '':
					print("object", objectType, remoteAddr[i][1], "\n", "subnet", remoteAddr[i][0], remoteAddr[i][2], file=open("../output/ipsec.txt", "a"))
				
		