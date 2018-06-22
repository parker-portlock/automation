import sys
import csv

#object group function

def CiscoTunGroup():
#opens CSVs
	with open('../files/ipsecForm.csv','rt') as ipsecForm:
		vpnForm = csv.reader(ipsecForm, delimiter = ',', quotechar = '|')
		vpnForm = list(vpnForm)
	with open('../files/localObjects.csv', 'rt') as csvLoc:
		localAddr = csv.reader(csvLoc, delimiter=',', quotechar='|')
		localAddr = list(localAddr)
	with open('../files/remoteObjects.csv', 'rt') as csvRem:
		remoteAddr = csv.reader(csvRem, delimiter=',', quotechar='|')
		remoteAddr = list(remoteAddr)

	#creates object group names
	localGroupName = 'VPN_'+ vpnForm[1][1] + '_LOCAL'
	remoteGroupName ='VPN_'+ vpnForm[1][1] + '_REMOTE'
	with open('../files/encGroups.csv', 'w', newline='') as csvEncGroup:
		groupWriter = csv.writer(csvEncGroup, delimiter = ',', quotechar = '|')
		groupWriter.writerow([localGroupName,remoteGroupName])
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

def CiscoGroup():
	groupName = input("What's the name for the object group? ")
	with open('../files/addr.csv', 'rt') as csvObj:
    		address = csv.reader(csvObj, delimiter=',', quotechar='|')
    		address = list(address)

	print("object-group network", groupName, file=open("../output/Objects.txt","a"))
	for i in range(len(address)):
		print("network-object object", address[i][1], file=open("../output/Objects.txt","a"))
	print("exit", file=open("../output/Objects.txt","a"))