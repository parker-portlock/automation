    #groupMod.py -> Quickly change objects in an object group
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
import paramiko
import getpass
import time
import os

loadFile = input ("Did you load the groupMod.csv in /files? (y/n) ")

if loadFile == "y":
    colnames = ['ADD','REMOVE']
    data = pandas.read_csv('../files/groupMod.csv', names=colnames, warn_bad_lines = True, error_bad_lines=False)
    add = data.ADD.tolist()
    remove = data.REMOVE.tolist()
    
    add = [a for a in add if str(a) != 'nan']
    remove = [r for r in remove if str(r) != 'nan']
    groupName = input("What object-group are we modifying? ")
    print ("conf t",file=open("../output/groupMod.txt","a"))
    print ("object-group network", groupName,file=open("../output/groupMod.txt","a"))
    for i in range(len(add)-1):
        print ("network-object host",add[i+1],file=open("../output/groupMod.txt","a"))
    
    for j in range(len(remove)-1):
        print ("no network-object host",remove[j+1],file=open("../output/groupMod.txt","a"))

    print ("end",file=open("../output/groupMod.txt","a"))
    
    with open('../output/groupMod.txt', 'r') as myfile:
        gmOutput=myfile.read()

   
    #SSH LOGIN
    ip = input("Hostname/IP: ")
    username = input("Username: ")
    password =  getpass.getpass("Password: ")
    remote_pre=paramiko.SSHClient()
    remote_pre.load_system_host_keys()
    remote_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    remote=remote_pre.invoke_shell()
    time.sleep(2)
    output=remote.recv(65535)
    print (output) 
    remote.send(gmOutput)
    time.sleep(2)
    output=remote.recv(65535)
    print(output)

    print ("Performing cleanup...")
    os.remove('../output/groupMod.txt')


else:
    print ("Invalid input. Exiting...")
    sys.exit()