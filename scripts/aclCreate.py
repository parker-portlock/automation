#extendedACL.py because we know da wae
import sys
import csv

def CiscoCryptoACL():
	with open('../files/encGroups.csv', 'rt') as csvGroupName:
		groupNames = csv.reader(csvGroupName, delimiter=',', quotechar='|')
		groupNames = list(groupNames)
	
	cmapACL = input("Please name your crypto map ACL: ")
	print("Creating crytpo map ACL...")
	for i in range(len(groupNames)):
		print ("access-list", cmapACL, "permit ip object-group", groupNames[i][0], "object-group", groupNames[i][1], file=open("../output/ipsec.txt","a"))
			
def CiscoFilterACL():		
	filterACL = input("Please name your VPN filter ACL: ")
	print("Creating VPN filter ACL...")
	print("access-list", filterACL, "deny any any", file=open("../output/ipsec.txt","a"))

	with open('../files/filterName.csv', 'w', newline='') as csvFilter:
		filterWriter = csv.writer(csvFilter, delimiter = ',', quotechar = '|')
		filterWriter.writerow([filterACL])