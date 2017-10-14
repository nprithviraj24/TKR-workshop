#Functions:

#Printing your college name and defining function.
def MyCollege():
    print "TKR College."

#calling the function

print "My college name is ",
MyCollege()

#Function with parameter(s)

def even_odd(a):
    if a%2 == 0:
        print a, " is an Even number."
    else:
        print a, "is a Odd number."


#Task 1
def two_numbers(a,b):
    sum = a+b
    print "Sum of the numbers: ", sum
    
    difference = a-b
    print "Difference between the numbers: ", difference

    multiply = a*b
    print "Multiplying the numbers: ", multiply
    