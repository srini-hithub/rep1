#!/usr/bin/python
#This is function is for the keyword length arguments.
def func1(*lst):
	sum=0
	for i in lst:
		sum+=i
	print("sum: ",sum)
	a=len(lst)
	print("number of the arguments: ",a)
#func1(25,45,45)
a=int(input("Enter the 1st argument: "))
b=int(input("Enter the 2nd argument: "))
func1(a,b)
