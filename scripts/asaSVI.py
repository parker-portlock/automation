    #asaSVI.py -> Quickly create Cisco ASA SVIs
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

loadFile = input ("Did you load the interface.csv in /files? (y/n) ")

if loadFile == "y":
    with open('../files/interface.csv', 'rt') as csvInt:
    	interface = csv.reader(csvInt, delimiter=',', quotechar='|')
    	interface = list(interface)   
    
    for i in range(len(interface)-1):
        intType = interface[i+1][0]
        intFunc = interface[i+1][1]
        netAddr = interface[i+1][2]
        netMask = interface[i+1][3]
        product = interface[i+1][4]

        netTup = netAddr.split(".")
        vlanNum = netTup[2]

        if intType == "internal":
            intFace = 8
            secLev = 80
        elif intType == "dmz":
            intFace = 9
            secLev = 25
        else:
            print ("Invalid Interface type. Exiting..")
            sys.exit()


        print ("interface te0/",intFace,".",vlanNum,sep="", file=open("../output/Interface.txt","a"))
        print ("vlan", vlanNum, file=open("../output/Interface.txt","a"))
        print ("nameif", product+"_"+intFunc+"_"+intType, file=open("../output/Interface.txt","a"))
        print ("security-level", secLev, file=open("../output/Interface.txt","a"))
        print ("ip address ",netTup[0],".",netTup[1],".",netTup[2],".1 ",netMask," standby ",netTup[0],".",netTup[1],".",netTup[2],".2 ",sep="", file=open("../output/Interface.txt","a"))


        objName = "ON_"+product+"_"+intFunc+"_"+intType
        print("object network", objName, file=open("../output/Interface.txt","a"))
        print("subnet", netAddr, netMask,file=open("../output/Interface.txt","a"))

        aclName = product+"_"+intFunc+"_"+intType+"_access_in"

        print ("access-list", aclName, "extended permit object-group active_directory object",objName,"object-group active_directory_servers", file=open("../output/Interface.txt","a"))
        print ("access-list", aclName, "extended permit object-group active_directory object",objName,"object-group active_directory_servers", file=open("../output/Interface.txt","a"))
        print ("access-list", aclName, "extended permit object-group kms object",objName," object-group kms_servers", file=open("../output/Interface.txt","a"))
        print ("access-list", aclName, "extended permit ip any object lbdmz_network", file=open("../output/Interface.txt","a"))
        print ("access-list", aclName, "extended permit tcp object",objName,"object-group shared_email_servers eq smtp", file=open("../output/Interface.txt","a"))
        print ("access-list", aclName, "extended permit tcp object",objName,"object-group shared_web_servers eq www", file=open("../output/Interface.txt","a"))
        print ("access-list", aclName, "extended permit tcp object",objName,"object-group shared_web_servers eq https", file=open("../output/Interface.txt","a"))
        print ("access-list", aclName, "remark Allow Access to Remote VPN Networks", file=open("../output/Interface.txt","a"))
        print ("access-list", aclName, "extended permit ip object",objName,"object-group remote_vpn_networks", file=open("../output/Interface.txt","a"))
        print ("access-list", aclName, "remark Block other private networks", file=open("../output/Interface.txt","a"))
        print ("access-list", aclName, "extended deny ip object",objName,"object-group rfc1918", file=open("../output/Interface.txt","a"))
        print ("access-list", aclName, "remark Allow access to all public networks", file=open("../output/Interface.txt","a"))
        print ("access-list", aclName, "extended permit ip object",objName,"any", file=open("../output/Interface.txt","a"))

        #print (netTup[0],netTup[1],netTup[2],netTup[3])
    print ("Done! You can find your script in /output/Interface.txt.")

else:
    print ("No File found. Exiting...")
    sys.exit()

