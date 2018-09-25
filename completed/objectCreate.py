    #ipsec.py -> Quickly create Cisco ikev1 and ikev2 tunnels
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
				print ("Invalid input... exiting program")
				sys.exit()
#Local object Creation
			objectType = "network"
			print("Let's create the local objects.")
			for i in range(len(localAddr)-1):
				netType = localAddr[i+1][2]
				if netType =='':
					print("object", objectType, localAddr[i+1][1], "\n", "host", localAddr[i+1][0], file=open("../output/ipsec.txt", "a"))
				elif netType !='':
					print("object", objectType, localAddr[i+1][1], "\n", "subnet", localAddr[i+1][0], localAddr[i+1][2], file=open("../output/ipsec.txt", "a"))

#Remote object Creation
			print("Let's create the remote objects.")
			for i in range(len(remoteAddr)-1):
				netType = remoteAddr[i+1][2]
				if netType =='':
					print("object", objectType, remoteAddr[i+1][1], "\n", "host", remoteAddr[i+1][0], file=open("../output/ipsec.txt", "a"))
				elif netType != '':
					print("object", objectType, remoteAddr[i+1][1], "\n", "subnet", remoteAddr[i+1][0], remoteAddr[i+1][2], file=open("../output/ipsec.txt", "a"))
				
