# Python Program to print the 
# 'n' lobes of DNA pattern 
import math


# Function to print upper half
# of the DNA or the upper lobe 
def printUpperHalf(str):
    first = 0
    second = 0
    pos = 0

    # Each half of the DNA is made of
    # combination of two compounds
    for i in range(1, 5):

        # Taking the two carbon
        # compounds from the string
        first = str[pos]
        second = str[pos + 1]
        pos += 2

        for j in range(4 - i, 0, -1):
            print(" ", end="")
        print(first, end="")
        for j in range(1, i):
            print("--", end="")
        print(second)

    # Function to print lower half


# of the DNA or the lower lobe
def printLowerHalf(str):
    first = 0
    second = 0
    pos = 0
    for i in range(1, 5):

        first = str[pos]
        second = str[pos + 1]
        pos += 2

        for j in range(1, i):
            print(" ", end="")
        print(first, end="")
        for j in range(4 - i, 0, -1):
            print("--", end="")
        print(second)

    # Function to print 'n' parts of DNA


def printDNA(str, n):
    for i in range(0, n):

        x = i % 6

        # Calling for upperhalf
        if (x % 2 == 0):
            printUpperHalf(str[x])
        else:

            # Calling for lowerhalf
            printLowerHalf(str[x])

        # driver code


n = 5

# combinations stored in the array 
DNA = ["ATTAATTA", "TAGCTAGC", "CGCGATAT",
       "TAATATGC", "ATCGTACG", "CGTAGCAT"]

printDNA(DNA, n)

# This code is contributed by Gitanjali. 
