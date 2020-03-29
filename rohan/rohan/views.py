
from django.shortcuts import render
#Library Management system
class Details :
     def __init__(self,name,mobile,year,stream):
            self.name=name
            self.mobile=mobile
            self.year=year
            self.stream=stream
        def ShowDetails():
            print("Name is :",self.name,"Mobile number : ",self.mobile,"You are currently studying in ",self.year,"You are doing ",self.stream)
        def updateDetails(name,mobile,year,stream):
            self.name = name
            self.mobile = mobile
            self.year = year
            self.stream = stream

print(__name__)
r1.Details("Rohan",8221988235,"Second","Computer Science")
print("\tEnter 1 for Show Details")
print("\tEnter 2 for update details")
i=input("Enter your choice")
if i==1:
    r1.showDetails()
elif i==2:
    r1.updateDetails(input("Enter name",input("Enter mobile"),input("Enter Year"),input("Enter stream")))
