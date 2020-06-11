#!/usr/bin/python
#This is the Python function to test the arguments.
#print ("This function is user defined function.")
def function():
	print("The number of arguments passed to the function are:")
	print("The arguments calling the main values.")
	print("This program requires the parameters.")
	value=input("Enter the values(with the space separated): ")
	l=list(value)
	length=len(l)
	print(l)
	print(length)

print(function())
