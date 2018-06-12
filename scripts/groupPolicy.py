import sys
import csv

def ciscoGroupPolicy():
    policyName = input("Please name your group policy: ")
    with open('../files/filterName.csv', 'rt') as csvFilter:
	    filterName = csv.reader(csvFilter, delimiter=',', quotechar='|')
	    filterName = list(filterName)

    addFilter = input("Apply the filter you created to the policy? (y/n) ")
    if addFilter == "y":

        print("group-policy", policyName, "internal")
        print("group-policy", policyName, "attributes")
        print("vpn-filter value", filterName[0])

        ikeVer = input("What IKE version are we using? (1/2) ")
        if ikeVer == "1":
            print("vpn-tunnel-protocol ikev1")
        elif ikeVer =="2":
            print("vpn-tunnel-protocol ikev2")
        else:
            print("Invalid input")

        print("exit")
    
    else:
        print("Exiting...")
        sys.exit()

    with open('../files/policyName.csv', 'w', newline='') as csvPolicy:
	    policyWriter = csv.writer(csvPolicy, delimiter = ',', quotechar = '|')
	    policyWriter.writerow([policyName,ikeVer])