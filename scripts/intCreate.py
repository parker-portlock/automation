import sys
import csv

csvLoad = input("Did you load the interface.csv to /files? (y/n)")
if csvLoad == 'y':
    print("Creating Interface Script...")

    with open('../files/interface.csv','rt') as interface:
        intForm = csv.reader(interface, delimiter = ',', quotechar = '|')
        intForm = list(interface)

    intType = intForm[1][0]
    prodName = intForm[1][1]
    func = intForm[1][2]
    netAddr = intForm[1][3]
    netMask = intForm[1][4]
    secLev = intForm[1][5]
    vlanNum = intForm[1][6]

    if intType == 'DMZ':
        print('placeholder')

    else:
        print('interface te0/8.', vlanNum, sep="", file=open("../output/interface.txt","a"))
        print('vlan ',vlanNum)
        print('nameif ', prodName,'_',func,'_',intType)
        print('security-level ',secLev)
        print('ip address ')