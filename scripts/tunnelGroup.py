import sys
import csv

def ciscoTunnelGroup():
    with open('../files/policyName.csv', 'rt') as csvPolicy:
	    policyName = csv.reader(csvPolicy, delimiter=',', quotechar='|')
	    policyName = list(policyName)
    
    peerIP = input("Please enter the remote peer IP: ")
    secondQuery = input("Do you have a secondary remote peer? (y/n)")
    if secondQuery == "y":
        secondaryIP = input("Pleace enter the secondary remote peer IP: ")
    else:
        "No secondary. Continuing..."
        print("tunnel-group", peerIP, "type ipsec-l2l")
        print("tunnel-group", peerIP, "general-attributes")
        print("default-group-policy", policyName[0])
        print 