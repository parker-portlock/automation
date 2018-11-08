import sys
import math

def maskToCidr():
    subnetMask = input ("Please Enter yoru subnet mask: ")
    maskTup = subnetMask.split(".")
    oct1 = maskTup[0]
    oct2 = maskTup[1]
    oct3 = maskTup[2]
    oct4 = maskTup[3]
    oct1bits = math.log2(int(oct1) + 1)
    oct2bits = math.log2(int(oct2) + 1)
    oct3bits = math.log2(int(oct3) + 1)
    oct4bits = math.log2(int(oct4) + 1)
    cidr = oct1bits + oct2bits + oct3bits + oct4bits
