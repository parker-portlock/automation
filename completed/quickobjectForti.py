    #quickObjectForti.py -> Quickly create network objects for the FortiOS platform
    #Copyright (C) 2018 Parker M. Portlock

    #This program is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License
    #along with this program.  If not, see <https://www.gnu.org/licenses/>.



import sys
import pandas
import csv
#import objectGroup

loadFile = input ("Did you load the objects into the addr.csv in /files? (y/n) ")

if loadFile == "y":
	with open('../files/addr.csv', 'rt') as csvObj:
		address = csv.reader(csvObj, delimiter=',', quotechar='|')
		address = list(address)

	for i in range(len(address)):
	    print ("edit", address[i][1], "\n", "set subnet", address[i][0] , address[i][2], "\n", "next", file=open("../output/pyFortiObject.txt", "a"))


groupQ = input("Do you want these in a group? (y/n)")
if groupQ == 'y':
	groupName = input("What's the name for the object group? ")

	colnames = ['ipaddr', 'hostname', 'subnetmask']
	data = pandas.read_csv('../files/addr.csv', names=colnames)
	hostnames = data.hostname.tolist()

	print ("config firewall addrgrp","\n", "edit", groupName, file=open("../output/pyFortiObject.txt","a"))	
	print ("set member", " ".join('"' + hostnames + '"' for hostnames in hostnames), file=open("../output/pyFortiObject.txt", "a"))
	print ("Output is in /output/Objects.txt")
else:
	print ("Output is in /output/Objects.txt")
	print ("Exiting...")
	sys.exit()