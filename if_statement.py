
# "If" Statements

""" 
A function that accepts 3 parameters and checks for equality between any two of them.
The function returns false when none of them are equal to any of the others.
"""
# function to return false
def max(a, b, c):
    if a != b and a != c and b != c:
        return False
    elif a == b == c:
        return True
    else:
        print(True)


f = max(2,4,5)
print(f)



# function to return True
def max(a, b, c):
    if a != b and a != c and b != c:
        return False
    elif a == b == c:
        return True
    else:
        print(True)


e = max(3,3,3)
print(e)


# function to return True
def max(a, b, c):
    if a != b and a != c and b != c:
        return False
    elif a == b == c:
        return True
    else:
        return True


g = max(2,3,3)
print(g)


#extra credit: modification of function to return True
def max(a, b, c):
    if (a != b and a != c and b != c):
        return False
    elif a == b == c:
        return True
    else:
        return True
        

h = max(6,5, int("5"))
print(h)