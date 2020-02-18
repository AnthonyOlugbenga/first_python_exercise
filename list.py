
# Lists

"""Create a global variable called myUniqueList. 
It should be an empty list to start.
"""

myUniqueList = []

def adding_element(*element):
    myUniqueList.extend(element)
    
    
adding_element(4,10,17,"6")
print(myUniqueList)


# it printed out myUniqueList = [4,10,17,"6"]
# adding 19 to the list through the function

myUniqueList = [4,10,17,"6"]

def adding_element(element):
    myUniqueList.append(element)

       
adding_element(19)
print(myUniqueList)


#adding number 10 to the list as duplicate, the number was not added and it returned False

myUniqueList = [4,10,17,"6",19]
output =[]

def adding_element(element):
    if element not in myUniqueList:
        myUniqueList.append(element)
        
        return True
    else:
            output.append(element)
    
            return False
    

f = adding_element(10)
print(f)
print(myUniqueList)
print(output)


#adding number 2 to the list, the number was added and it returned True

myUniqueList = [4,10,17,"6",19]
output =[]

def adding_element(element):
    if element not in myUniqueList:
        myUniqueList.append(element)
        
        return True
    else:
            output.append(element)
    
            return False
    

f = adding_element(2)
print(f)
print(myUniqueList)
print(output)




# extra credit for rejected input

myUniqueList = [4,10,17,"6",19]
myLeftovers =[]

def adding_element(element):
    
    if element not in myUniqueList:
        myUniqueList.append(element)
        
        return True
    else:
            myLeftovers.append(element)
    
            return False
    

f = adding_element(4)
print(f)
print(myUniqueList)
print(myLeftovers)