import objectCreate
import objectGroup
import sys
import csv

print ("Creating objects and groups...")
objectCreate.CiscoObject()
objectGroup.CiscoGroup()

print ("Creating crypto-map ACL...")
with open('../files/encGroups.csv', 'rt') as csvGroupName:
	groupNames = csv.reader(csvGroupName, delimiter=',', quotechar='|')
	groupNames = list(groupNames)
cmapACL = input("Please name your crypto map ACL: ")
for i in range(len(groupNames)):
	print ("access-list", cmapACL, "permit ip object-group", groupNames[i][0], "object-group", groupNames[i][1], file=open("../output/ipsec.txt","a"))



print ("Creating VPN filter ACL...")
filterACL = input("Please name your VPN filter ACL: ")
print("access-list", filterACL, "deny any any", file=open("../output/ipsec.txt","a"))

print ("Creating group policy...")
#group policy creation
policyName = input("Please name your group policy: ")
with open('../files/filterName.csv', 'rt') as csvFilter:
    filterName = csv.reader(csvFilter, delimiter=',', quotechar='|')
    filterName = list(filterName)

addFilter = input("Apply the filter you created to the policy? (y/n) ")
if addFilter == "y":

    print("group-policy", policyName, "internal", file=open("../output/ipsec.txt","a"))
    print("group-policy", policyName, "attributes", file=open("../output/ipsec.txt","a"))
    print("vpn-filter value", filterName[0], file=open("../output/ipsec.txt","a"))

    ikeVer = input("What IKE version are we using? (1/2) ")
    if ikeVer == "1":
        print("vpn-tunnel-protocol ikev1", file=open("../output/ipsec.txt","a"))
    elif ikeVer =="2":
        print("vpn-tunnel-protocol ikev2", file=open("../output/ipsec.txt","a"))
    else:
        print("Invalid input")
        sys.exit()
    
else:
    print("Exiting...")
    sys.exit()


print ("Creating tunnel-group configuration...")
#tunnel-group config
peerIP = input("Please enter the remote peer IP: ")
print("tunnel-group", peerIP, "type ipsec-l2l", file=open("../output/ipsec.txt","a"))
print("tunnel-group", peerIP, "general-attributes", file=open("../output/ipsec.txt","a"))
print("default-group-policy", policyName, file=open("../output/ipsec.txt","a"))
print("tunnel-group", peerIP, "ipsec-attributes", file=open("../output/ipsec.txt","a"))

secondQuery = input("Do you have a secondary remote peer? (y/n)")
if secondQuery == "y":
    secondaryIP = input("Pleace enter the secondary remote peer IP: ")
    print("tunnel-group", secondaryIP, "type ipsec-l2l", file=open("../output/ipsec.txt","a"))
    print("tunnel-group", secondaryIP, "general-attributes", file=open("../output/ipsec.txt","a"))
    print("default-group-policy", policyName, file=open("../output/ipsec.txt","a"))
    print("tunnel-group", secondaryIP, "ipsec-attributes", file=open("../output/ipsec.txt","a"))
else:
    "No secondary. Continuing..."
    
if ikeVer == "1":
    psk = input("Please enter your PSK: ")
    print("ikev1 pre-shared-key", psk, file=open("../output/ipsec.txt","a"))
elif ikeVer =="2":
    remotePSK = input("Please enter your remote PSK: ")
    localPSK = input("Please enter your local PSK: ")
    print("ikev2 remote-authentication pre-shared-key", remotePSK, file=open("../output/ipsec.txt","a"))
    print("ikev2 local-authentication pre-shared-key", localPSK, file=open("../output/ipsec.txt","a"))
else:
    print("go kick rocks")

print ("Configuring crypto map...")
#Crypto Map configuration
cmapIndex = input("Please enter the crypto map index number: ")
outsideMapName = input("Please enter your outside-map name: ")
transformSet = input("Please enter the appropriate transform-set: ")
phase1Mode = input("Please enter your Phase 1 mode: ")
print("crypto map", outsideMapName, cmapIndex, "match address", cmapACL)
print("crypto map", outsideMapName, cmapIndex, "ikev1 transform-set", transformSet)
print("crypto map", outsideMapName, cmapIndex, "ikev1 phase1-mode", phase1Mode)
pfs = input("Do you want to enable PFS? (y/n)")
if pfs == "y":
    dhGroup = input("What DH group should be set? ")
    print("crypto map", outsideMapName, cmapIndex, "set pfs", dhGroup)
else:
    print("Setting defaults...")
    print("crypto map", outsideMapName, cmapIndex, "set pfs")
if secondQuery == "y":
    print("crypto map", outsideMapName, cmapIndex, "set peer", peerIP, secondaryIP)
else:
    print("crypto map", outsideMapName, cmapIndex, "set peer", peerIP)
    

#print ("Your IPSec tunnel configuration is complete. Use the output located in /output/ipsec.txt.")