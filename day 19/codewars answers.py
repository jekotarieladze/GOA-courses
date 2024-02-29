#question 1

# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

# Initialising a list 
findNeedle = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
print("here is the list", findNeedle)

# Printing the index of "needle" in the list 
print("found the needle at position", findNeedle.index("needle"))


print("the question 1 is done now for the question 2")
#question 2

#Write a function which converts the input string to uppercase.

def make_upper_case():
    user_input=str(input("what should i make uppercase??"))
    print(user_input.upper())

make_upper_case()

print("question 2 done now onto the question 3")

#question 3

# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2

# Input: []
# Output: 0

# Input: [-2.398]
# Output: -2.398

# Assumptions
# You can assume that you are only given numbers.
# You cannot assume the size of the array.
# You can assume that you do get an array and if the array is empty, return 0.

#input option 1
print("input option 2")


def sum_array():
    arr = [1, 5.2, 4, 0, -1]
    print("the list is ", arr)
    print("the sum of this list", sum(arr))

sum_array()


#input option 2
print("input option 2")


def another_one():
    arr1 = []
    print("here the list is ", arr1)
    print("the sum of this list", sum(arr1))
    
another_one()


#input option 3
print("input option 3")


def second_one():
    arr2 = [-2.398]
    print("this is the elements contained in the list", arr2)
    print("the sum of this list", sum(arr2))
    
second_one()


#question 4
print("question3 done now onto the question 4")

# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

def are_you_playing_banjo():
    name1=("Randy")
    name2=("Lisa")
    first_one=(name1.find("R,r"))
    sechond_one=(name2.find("R,r"))
    if first_one == "R,r":
        print (name1, " plays banjo")
    else:
        print (name1, " does not play banjo")
               
               
    if sechond_one == "R,r":
        print (name1, " plays banjo")
    else:
        print (name1, " does not play banjo")

are_you_playing_banjo()


#question 5
print("question 4 done now its time for question 5")

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []

print("couldn't really understand what to do")

print("couldnt finish question 5 so lets move onto question 6")

# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

def find_average():
    numbers=[2,5,3,7,8,5,10]
    average= sum(numbers)/len(numbers)
    print("average of this list is ", round(average))
    
find_average()

print("done thank you for reading or whatever BYEE (stan blackpink)")