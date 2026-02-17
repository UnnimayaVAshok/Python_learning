#without parameters
def details():
    name = input("Enter the name")
    return name
name = details()
print(name)

#with parameters
def data(name,mark):
    print(name,mark)
data('Arya',10)

#optional parameter
def mark(id,eligible = True):
    if eligible :
        print(str(id)+" Passed")
mark(43)
    
