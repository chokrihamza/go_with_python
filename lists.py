# list to store mult items 
# ordered
# changeable 
# allow duplication

list0=["tomato","apple","banans"]
list1=[1,2,3]
list2=["dlgf",2,13,'dflkdf']
print(list0,list1,list2)
print(len(list0),type(list0))
list3=list(('1',2,3,4))
print(list3,list3[0],list3[1],list3[len(list3)-1])
print(list3[0:2],list3[2:])
ref=list3
print(2 in list3)
ref[0]=10
print(list3)