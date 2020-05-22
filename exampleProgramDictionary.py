# prog that collects info and stores in a dictionary
# name,age,edu,contact,area from the user

name=input("Enter your Name")
age=input("Enter your age ")
edu=input("Enter your edu ")
contact=input("Enter your phone number ")
area=input("Enter where you live ")

# define a dict to store all the data

details={}

# add all the values to the dict
# creating a new key-value pair
# DictName['NewKey']="New value"

details["name"]=name
details["age"]=age
details["edu"]=edu
details["contact"]=contact
details["area"]=area


# display the dictionary

print(details)
