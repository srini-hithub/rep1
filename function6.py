#!/usr/bin/python
#This is to define the keyword length arguments.
def func2(**kwargs):
	for i,j in kwargs.items():
		print(i,"=",j)

func2(name="name1",age=23)
