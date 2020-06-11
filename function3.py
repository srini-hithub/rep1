#!/usr/bin/python
#This is for the default arguments.
def func1(a,b="student"):
	print("name: ",a)
	print("Proffession: ",b) 

#To call the function.
print(func1("name1"))
print(func1(a="name2",b="employee"))
print(func1(b="worker",a="name3"))
