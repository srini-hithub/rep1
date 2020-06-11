#!/usr/bin/python
print ("This program to build the employee data base")
dict={}
count=1
while count <=10:
	emp=input("Enter the employee number:")
	if emp == "none":
		print ("input should be number")
	detail1=input("Enter the Name of the employee:")
	detail2=input("Enter the age of the employee:")
	detail3=input("Enter the mobile number of the employee:")
	dict[emp]=[detail1,detail2,detail3]
	count += 1
print (dict)
