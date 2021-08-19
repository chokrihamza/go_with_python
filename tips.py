#from math import pi
#print([str(round(pi,i)) for i in range(10)])
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],]
# first 
print([[row[i] for row in matrix] for i in range(4)] )
# or just 
print(list(zip(*matrix)))

#del matrix
print(matrix)

t=1,2,2,3,[1,2,3]
print(t)
#unpack
_,_,_,_,x=t
print(x)
last=t,(1,2,3)
print(last)
# lets talk about sets 
x=set("12345")
y=set("345789")
print(x)
print(y)
print(x-y)
print(x|y)
print(x&y)
print(x^y)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

#dictionaries
dict1=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict1)

dict2={f'intem{x}':x**3 for x in range(10)}
print(dict2.items())
print((1, 2, 3, 4)<(1, 2, 5))