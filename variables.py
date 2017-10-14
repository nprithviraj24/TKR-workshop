#This file deals with secondary variables

#Type 1: LIST
print("List")
l = [1,2,3,4,5]
print(l)
print(type(l))

#iterating through each of the elements in lists
for i in l:
    print(i)
# NOTE: Please maintain the indentations.

#Multiplying each element with 2
for i in l:
    print(i*2)

#Let print the length of the list
print("\n Length of list: "),
print(len(l))

#Type 2 Set
print("\n\n")
print("Type 2: Set")
#SET will not allow duplicates.
S = {7,8,9}

for i in S:
    print(i)
#EXERCISE: Try inserting duplicate value and execute the program.

#Type 3: Dictionary
print("\n\n")
print("Type 3: Dictionary")

d = {"name": "TKR", "location": "Hyderabad"}

# The comma after a print statement is used to indicate interpreter that we are continuing in the same line. 
print("Details: ")
print "Name of the college: ",
print d["name"]
print "Location of the college: ",
print d["location"]