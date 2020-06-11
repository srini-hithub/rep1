#!/bin/python
print ("This program is to test the commandline argurments:")
import sys
n=len(sys.argv)
args=sys.argv
print ("Number of command line arguments:",n)
print ("The command line arguments you entered are:", args)
print ("Argurments one by one:")
for i in args:
	print(i)
