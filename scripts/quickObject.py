import sys
import csv
import objectGroup

loadFile = input ("Did you load the objects into the addr.csv in /files? (y/n) ")

if loadFile == "y":
	with open('../files/addr.csv', 'rt') as csvObj:
		address = csv.reader(csvObj, delimiter=',', quotechar='|')
		address = list(address)

	for i in range(len(address)):
	    netType = address[i][2]
	    if netType =='':
	    	print("object network", address[i][1], "\n", "host", address[i][0], file=open("../output/Objects.txt", "a"))
	    elif netType !='':
	        print("object netowrk", address[i][1], "\n", "subnet", address[i][0], address[i][2], file=open("../output/Objects.txt", "a"))


groupQ = input("Do you want these in a group? (y/n)")
if groupQ == 'y':
	groupName = input("What's the name for the object group? ")
	print("object-group network", groupName, file=open("../output/Objects.txt","a"))
	for i in range(len(address)):
		print("network-object object", address[i][1], file=open("../output/Objects.txt","a"))
	print("exit", file=open("../output/Objects.txt","a"))
	print ("Output is in /output/Objects.txt")
else:
	print ("Output is in /output/Objects.txt")
	print("Exiting...")
	sys.exit()