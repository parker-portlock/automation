    #quickObject.py -> Quickly create Cisco network objects for the ASA platform (specialized for tunnels)
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
import csv
import objectGroup

loadFile = input ("Did you load the objects into the addr.csv in /files? (y/n) ")


if loadFile == "y":
	with open('../files/addr.csv', 'rt') as csvObj:
		address = csv.reader(csvObj, delimiter=',', quotechar='|')
		address = list(address)

	for i in range(len(address)-1):
		mask = address [i+1][2]
		maskTup = mask.split(".")
		hostBit = maskTup[3]
		#print(hostBit)

		if hostBit == "255":
			print("object network", address[i+1][1], "\n", "host", address[i+1][0], file=open("../output/Objects.txt", "a"))
	    
		else:
			print("object network", address[i+1][1], "\n", "subnet", address[i+1][0], address[i+1][2], file=open("../output/Objects.txt", "a"))
		


groupQ = input("Do you want these in a group? (y/n)")
if groupQ == 'y':
	groupName = input("What's the name for the object group? ")
	print("object-group network", groupName, file=open("../output/Objects.txt","a"))
	for i in range(len(address)-1):
		print("network-object object", address[i+1][1], file=open("../output/Objects.txt","a"))
	print("exit", file=open("../output/Objects.txt","a"))
	print ("Output is in /output/Objects.txt")
else:
	print ("Output is in /output/Objects.txt")
	print("Exiting...")
	sys.exit()