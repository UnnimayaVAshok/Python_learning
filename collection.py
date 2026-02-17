#list mutable and heterogeneous
names = []
names.append('Arya')
names.append('Krishna')
names.append('5')
print(names)
names.reverse()
print(names)
print(names.index('Krishna'))
names.remove('Arya')
print(names)

#array immutable and homogeneous
#from array import array
from array import array
arr = array('i', [1,2,3])
#arr = [1,2,3]
print(list(arr))
arr.append(4)
print(list(arr))
arr.remove(2)
print(arr)

#dictionary
details = {'name' : 'Arya','place' : 'piravom'}
print(details)
n = details.get('name')
print("Name is : "+n)
details.update({'Mark' : 10})
print(details)
