import objectCreate
import objectGroup
import sys
import csv

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
print("access-list", filterACL, "extended deny any any", file=open("../output/ipsec.txt","a"))

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
else:
    "No secondary. Continuing..."
  
if ikeVer == "1":
    print("ikev1 pre-shared-key", "<ENTER PSK HERE>", file=open("../output/ipsec.txt","a"))
elif ikeVer =="2":
    print("ikev2 remote-authentication pre-shared-key", "<REMOTE PSK>", file=open("../output/ipsec.txt","a"))
    print("ikev2 local-authentication pre-shared-key", "<LOCALPSK>", file=open("../output/ipsec.txt","a"))
else:
    print("GO KICK ROCKS")

print ("Configuring crypto map...")
#Crypto Map configuration
cmapIndex = vpnForm[1][10]
outsideMapName = vpnForm[1][11]
p2Prop = vpnForm[1][5]
p2Life = vpnForm[1][12]
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
    

#print ("Your IPSec tunnel configuration is complete. Use the output located in /output/ipsec.txt.")