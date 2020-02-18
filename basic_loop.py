# Basic Loops

# Write a program that prints the numbers from 1 to 100

"""
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""

 for x in range(1,101):
        if x%3==0 and x%5==0:
            print("FizzBuzz")
        elif x%3==0:
             print("Fizz")
        elif x%5==0:
            print("Buzz")
        else:
            print(x)



# Extra Credit:

 for x in range(1,101):
        if x%3==0 and x%5==0:
            print("FizzBuzz")
        elif x%3==0:
             print("Fizz")
        elif x%5==0:
            print("Buzz")
        elif x%x==0 and x%1==0:
            print("prime")
        else:
            print(x)