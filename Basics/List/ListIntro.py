#Lists are used to store multiple items in a single variable.

from numpy import append


myList=["hello", "Rollno", 21]
#List index is fixed and if we want to add something we can append it at end of the list
myList.append(28)
print(myList)
print(myList[1])

#allow duplicates in it
duplist = ["apple", "banana", "oranges", "banana"]
print(duplist)

#List length
print(len(duplist))

#type
#lists are defined as objects with the data type 'list':
print(type(duplist))

#We can make list using list constructor 
conslist=list(("Alola" , "Aregato Gojaimas"))
print(conslist) 

conslist[0]="hello"
print(conslist)