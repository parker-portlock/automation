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


import objectCreate
import objectGroup
import paramiko
import getpass
import time 
import os 
import sys 
import csv

print ('conf t', file=open("../output/ipsec.txt","a"))

with open('../files/ipsecForm.csv','rt') as ipsecForm:
    vpnForm = csv.reader(ipsecForm, delimiter = ',', quotechar = '|')
    vpnForm = list(vpnForm)

print("Starting...")
objectCreate.CiscoTunObject()
objectGroup.CiscoTunGroup()

#crypto-map ACL creation
print ("Creating crypto-map ACL...")
with open('../files/encGroups.csv', 'rt') as csvGroupName:
	groupNames = csv.reader(csvGroupName, delimiter=',', quotechar='|')
	groupNames = list(groupNames)
cmapACL = 'VPN_'+ vpnForm[1][1] + '_CMAP'
for i in range(len(groupNames)):
	print ("access-list", cmapACL, "extended permit ip object-group", groupNames[i][0], "object-group", groupNames[i][1], file=open("../output/ipsec.txt","a"))

#vpn filter ACL creation
print ("Creating VPN filter ACL...")
filterACL ='VPN_'+ vpnForm[1][1] + '_FLTR'
print("access-list", filterACL, "extended deny ip any any", file=open("../output/ipsec.txt","a"))

#group policy creation
print ("Creating group policy...")
policyName = 'VPN_'+ vpnForm[1][1] + '_POLICY'
print("group-policy", policyName, "internal", file=open("../output/ipsec.txt","a"))
print("group-policy", policyName, "attributes", file=open("../output/ipsec.txt","a"))
print("vpn-filter value", filterACL, file=open("../output/ipsec.txt","a"))

#determine IKE version
ikeVer = vpnForm[1][2]
if ikeVer == "1":
    print("vpn-tunnel-protocol ikev1", file=open("../output/ipsec.txt","a"))
elif ikeVer =="2":
    print("vpn-tunnel-protocol ikev2", file=open("../output/ipsec.txt","a"))
else:
    print("Invalid input")
    sys.exit()

print("exit", file=open("../output/ipsec.txt","a"))


#tunnel-group config
print ("Creating tunnel-group configuration...")
peerIP = vpnForm[1][3]
print("tunnel-group", peerIP, "type ipsec-l2l", file=open("../output/ipsec.txt","a"))
print("tunnel-group", peerIP, "general-attributes", file=open("../output/ipsec.txt","a"))
print("default-group-policy", policyName, file=open("../output/ipsec.txt","a"))
print("tunnel-group", peerIP, "ipsec-attributes", file=open("../output/ipsec.txt","a"))


secondaryIP = vpnForm[1][4]
if secondaryIP != "":
    print("tunnel-group", secondaryIP, "type ipsec-l2l", file=open("../output/ipsec.txt","a"))
    print("tunnel-group", secondaryIP, "general-attributes", file=open("../output/ipsec.txt","a"))
    print("default-group-policy", policyName, file=open("../output/ipsec.txt","a"))
    print("tunnel-group", secondaryIP, "ipsec-attributes", file=open("../output/ipsec.txt","a"))
    print("exit", file=open("../output/ipsec.txt","a"))
else:
    "No secondary. Continuing..."
  
if ikeVer == "1":
    print("ikev1 pre-shared-key", "<ENTER PSK HERE>", file=open("../output/ipsec.txt","a"))
    print("exit", file=open("../output/ipsec.txt","a"))
elif ikeVer =="2":
    print("ikev2 remote-authentication pre-shared-key", "REMOTEPSK", file=open("../output/ipsec.txt","a"))
    print("ikev2 local-authentication pre-shared-key", "LOCALPSK", file=open("../output/ipsec.txt","a"))
    print("exit", file=open("../output/ipsec.txt","a"))
else:
    print("GO KICK ROCKS")


print ("Configuring crypto map...")
#Crypto Map configuration
cmapIndex = vpnForm[1][10]
outsideMapName = vpnForm[1][11]
p2Prop = vpnForm[1][5]
p2Life = vpnForm[1][6]
if ikeVer == "1":
    ikeNegMode = vpnForm[1][9]
    print("crypto map", outsideMapName, cmapIndex, "set ikev1 phase1-mode", ikeNegMode, file=open("../output/ipsec.txt","a"))
    print("crypto map", outsideMapName, cmapIndex, "set ikev1 transform-set", p2Prop, file=open("../output/ipsec.txt","a"))
elif ikeVer =="2":
    print("crypto map", outsideMapName, cmapIndex, "set ikev2 ipsec-proposal", p2Prop, file=open("../output/ipsec.txt","a"))
else:
    print("Invalid IKE version. Exiting...")
    sys.exit()


print("crypto map", outsideMapName, cmapIndex, "match address", cmapACL, file=open("../output/ipsec.txt","a"))
print("crypto map", outsideMapName, cmapIndex, "set security-association lifetime seconds", p2Life, file=open("../output/ipsec.txt","a"))

pfs = vpnForm[1][7]
if pfs == "y":
    dhGroup = vpnForm[1][8]
    print("crypto map ", outsideMapName," ",cmapIndex, " set pfs group", dhGroup, sep="", file=open("../output/ipsec.txt","a"))
else:
    print("Setting defaults...")
if secondaryIP == "y":
    print("crypto map", outsideMapName, cmapIndex, "set peer", peerIP, secondaryIP, file=open("../output/ipsec.txt","a"))
else:
    print("crypto map", outsideMapName, cmapIndex, "set peer", peerIP, file=open("../output/ipsec.txt","a"))
    
print ('end', file=open("../output/ipsec.txt","a"))
print ('wr mem', file=open("../output/ipsec.txt","a"))

#READ OUTPUT FILE
with open('../output/ipsec.txt', 'r') as myfile:
     ipsec=myfile.read()

#SSH LOGIN
ip = input("Enter target ASA IP: ")
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
remote.send(ipsec)
time.sleep(2)
output=remote.recv(100000)
print(output)

print ("Performing cleanup...")
os.remove('../output/ipsec.txt')

print ("Your IPSec tunnel configuration is complete.")
